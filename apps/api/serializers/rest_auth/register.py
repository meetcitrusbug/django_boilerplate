"""
This is a Serializer module.
Define your custom serializers here.
"""

import random
import string

from django.contrib.auth import get_user_model
from django.http import HttpRequest
from django.utils.translation import ugettext_lazy as _
from requests.exceptions import HTTPError
from rest_framework import serializers, status

try:
    from allauth.account import app_settings as allauth_settings
    from allauth.account.adapter import get_adapter
    from allauth.account.utils import setup_user_email
    from allauth.socialaccount.helpers import complete_social_login
    from allauth.socialaccount.models import SocialAccount
    from allauth.socialaccount.providers.base import AuthProcess
    from allauth.utils import email_address_exists, get_username_max_length
except ImportError:
    raise ImportError("allauth needs to be added to INSTALLED_APPS.")

# from social.utils import CustomValidation

# -----------------------------------------------------------------------------
# Register serializer
# -----------------------------------------------------------------------------


class SocialAccountSerializer(serializers.ModelSerializer):

    """
    serialize allauth SocialAccounts for use with a REST API
    """
    class Meta:
        """Define serializer properties in Meta class"""

        model = SocialAccount
        fields = (
            'id',
            'provider',
            'uid',
            'last_login',
            'date_joined',
        )


class SocialLoginSerializer(serializers.Serializer):
    """
    Custom serializer
    """

    access_token = serializers.CharField(required=False, allow_blank=True)
    code = serializers.CharField(required=False, allow_blank=True)

    def _get_request(self):
        request = self.context.get('request')
        if not isinstance(request, HttpRequest):
            request = request._request
        return request

    def get_social_login(self, adapter, app, token, response):
        """
        :param adapter: allauth.socialaccount Adapter subclass.
            Usually OAuthAdapter or Auth2Adapter
        :param app: `allauth.socialaccount.SocialApp` instance
        :param token: `allauth.socialaccount.SocialToken` instance
        :param response: Provider's response for OAuth1. Not used in the
        :returns: A populated instance of the
            `allauth.socialaccount.SocialLoginView` instance
        """
        request = self._get_request()
        social_login = adapter.complete_login(request, app, token, response=response)
        social_login.token = token
        return social_login

    def validate(self, attrs):
        view = self.context.get('view')
        request = self._get_request()

        if not view:
            raise serializers.ValidationError(
                _("View is not defined, pass it as a context variable")
            )

        adapter_class = getattr(view, 'adapter_class', None)
        if not adapter_class:
            raise serializers.ValidationError(_("Define adapter_class in view"))

        adapter = adapter_class(request)
        app = adapter.get_provider().get_app(request)

        # More info on code vs access_token
        # http://stackoverflow.com/questions/8666316/facebook-oauth-2-0-code-and-token

        # Case 1: We received the access_token
        if attrs.get('access_token'):
            access_token = attrs.get('access_token')

        # Case 2: We received the authorization code
        elif attrs.get('code'):
            self.callback_url = getattr(view, 'callback_url', None)
            self.client_class = getattr(view, 'client_class', None)

            if not self.callback_url:
                raise serializers.ValidationError(
                    _("Define callback_url in view")
                )
            if not self.client_class:
                raise serializers.ValidationError(
                    _("Define client_class in view")
                )

            code = attrs.get('code')

            provider = adapter.get_provider()
            scope = provider.get_scope(request)
            client = self.client_class(
                request,
                app.client_id,
                app.secret,
                adapter.access_token_method,
                adapter.access_token_url,
                self.callback_url,
                scope
            )
            token = client.get_access_token(code)
            access_token = token['access_token']

        else:
            raise serializers.ValidationError(
                _("Incorrect input. access_token or code is required."))

        social_token = adapter.parse_token({'access_token': access_token})
        social_token.app = app

        try:
            login = self.get_social_login(adapter, app, social_token, access_token)
            complete_social_login(request, login)
        except HTTPError:
            raise serializers.ValidationError(_("Incorrect value"))

        if not login.is_existing:
            if not login.user.email:
                letters_and_digits = string.ascii_letters + string.digits
                result_str = ''.join((random.choice(letters_and_digits) for i in range(16)))
                login.user.email = result_str + '@onedrop.com'
            # We have an account already signed up in a different flow
            # with the same email address: raise an exception.
            # This needs to be handled in the frontend. We can not just
            # link up the accounts due to security constraints
            if allauth_settings.UNIQUE_EMAIL:
                # Do we have an account already with this email address?
                account_exists = get_user_model().objects.filter(
                    email=login.user.email,
                ).exists()
                if account_exists:
                    raise serializers.ValidationError(
                        _("User is already registered with this e-mail address.")
                    )

            login.lookup()
            login.save(request, connect=True)

        attrs['user'] = login.account.user

        return attrs


class SocialConnectMixin(object):
    def get_social_login(self, *args, **kwargs):
        """
        Set the social login process state to connect rather than login
        Refer to the implementation of get_social_login in base class and to the
        allauth.socialaccount.helpers module complete_social_login function.
        """
        social_login = super(SocialConnectMixin, self).get_social_login(*args, **kwargs)
        social_login.state['process'] = AuthProcess.CONNECT
        return social_login


class SocialConnectSerializer(SocialConnectMixin, SocialLoginSerializer):
    """
    Custom serializer
    """

    pass


class RegisterSerializer(serializers.Serializer):
    """
    Custom serializer
    """

    name = serializers.CharField()
    email = serializers.EmailField(required=allauth_settings.EMAIL_REQUIRED)

    # user_type = serializers.CharField(write_only=True)

    mobile = serializers.CharField()
    # company = serializers.CharField(required=False)

    username = serializers.CharField(
        max_length=get_username_max_length(),
        min_length=allauth_settings.USERNAME_MIN_LENGTH,
        required=False
    )
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    gender = serializers.CharField(required=False)
    dob = serializers.CharField(required=False)
    avatar = serializers.ImageField(required=False)

    def validate_username(self, username):
        """Checks for username validation"""
        username = get_adapter().clean_username(username)
        return username

    def validate_email(self, email):
        """Checks for email validation"""
        email = get_adapter().clean_email(email)
        if allauth_settings.UNIQUE_EMAIL:
            if email and email_address_exists(email):
                msg = _("A user is already registered with this e-mail address.")
                # raise serializers.ValidationError(_("A user is already registered with this e-mail address."))
                raise CustomValidation(msg, status_code=status.HTTP_200_OK)

        return email

    def validate_password1(self, password):
        """Checks for password1 validation"""
        return get_adapter().clean_password(password)

    def validate(self, data):
        """Override this method to validate registration attributes"""
        if data['password1'] != data['password2']:
            msg = _("The two password fields didn't match.")
            # raise serializers.ValidationError(_("The two password fields didn't match."))
            raise CustomValidation(msg, status_code=status.HTTP_200_OK)

        return data

    def custom_signup(self, request, user):
        """Define custom signup here"""
        pass

    def get_cleaned_data(self):
        """Get cleaned data from the HTML form"""
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            'mobile': self.validated_data.get('mobile', ''),
            'gender': self.validated_data.get('gender', ''),
            'name': self.validated_data.get('name', ''),
            'dob': self.validated_data.get('dob', ''),
            'avatar': self.validated_data.get('avatar', ''),
            # 'user_type': self.validated_data.get('user_type', ''),
        }

    def save(self, request):
        """Override save method to store data into the database"""
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()

        adapter.save_user(request, user, self)
        self.custom_signup(request, user)
        setup_user_email(request, user, [])
        return user


class VerifyEmailSerializer(serializers.Serializer):
    """
    Custom serializer
    """
    key = serializers.CharField()
