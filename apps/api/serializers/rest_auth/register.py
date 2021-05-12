"""
This is a Serializer module.
Define your custom serializers here.
"""

from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers, status

try:
    from allauth.account import app_settings as allauth_settings
    from allauth.account.adapter import get_adapter
    from allauth.account.utils import setup_user_email
    from allauth.utils import email_address_exists, get_username_max_length
except ImportError:
    raise ImportError("allauth needs to be added to INSTALLED_APPS.")

class RegisterSerializer(serializers.Serializer):
    """
    Custom serializer
    """

    name = serializers.CharField()
    email = serializers.EmailField(required=allauth_settings.EMAIL_REQUIRED)

    mobile = serializers.CharField()

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
                raise CustomValidation(msg, status_code=status.HTTP_200_OK)

        return email

    def validate_password1(self, password):
        """Checks for password1 validation"""
        return get_adapter().clean_password(password)

    def validate(self, data):
        """Override this method to validate registration attributes"""
        if data['password1'] != data['password2']:
            msg = _("The two password fields didn't match.")
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
