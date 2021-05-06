from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.twitter.views import TwitterOAuthAdapter
from allauth.socialaccount.providers.apple.views import AppleOAuth2Adapter
from rest_auth.registration.views import SocialLoginView
from rest_auth.registration.serializers import SocialLoginSerializer
from rest_auth.social_serializers import TwitterLoginSerializer
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from allauth.socialaccount.providers.apple.client import AppleOAuth2Client

import random
import string
from rest_auth.app_settings import JWTSerializer
from rest_auth.utils import jwt_encode
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from . apiviews import MyAPIView
from . models import User


class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter
    client_class = OAuth2Client
    serializer_class = SocialLoginSerializer


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    client_class = OAuth2Client
    serializer_class = SocialLoginSerializer


class TwitterLogin(SocialLoginView):
    adapter_class = TwitterOAuthAdapter
    client_class = OAuth2Client
    serializer_class = TwitterLoginSerializer


class AppleLoginAPIView(MyAPIView):
    """
    API View to login using Apple ID.
    """
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        success_message = "User verified successfully!"
        unsuccess_message = "It seems like this Email address is already registered with different login method!"
        try:
            token = request.data["access_token"]
            if "email" in request.data and request.data["email"] != "":
                email = request.data["email"]

                user_data = User.objects.filter(email=email, apple_token=token)
                if user_data.exists():
                    user = user_data.get()
                    token = jwt_encode(user)
                    data = {
                        'user': user,
                        'token': token
                    }
                    serializer = JWTSerializer(instance=data)
                    return Response({
                        "status": "OK",
                        "message": success_message,
                        "data": serializer.data
                    })

                else:
                    instance = User()
                    instance.email = email
                    instance.apple_token = token
                    instance.save()
                    user = User.objects.get(id=instance.id)
                    token = jwt_encode(user)
                    data = {
                        'user': user,
                        'token': token
                    }
                    serializer = JWTSerializer(instance=data)
                    return Response({
                        "status": "OK",
                        "message": success_message,
                        "data": serializer.data
                    })

            else:

                user_data = User.objects.filter(apple_token=token)
                if user_data.exists():
                    user = user_data.get()
                    token = jwt_encode(user)
                    data = {
                        'user': user,
                        'token': token
                    }
                    serializer = JWTSerializer(instance=data)
                    return Response({
                        "status": "OK",
                        "message": success_message,
                        "data": serializer.data
                    })

                else:
                    letters_and_digits = string.ascii_letters + string.digits
                    result_str = ''.join((random.choice(letters_and_digits) for i in range(8)))
                    instance = User()
                    instance.email = result_str + '@onedrop.com'
                    instance.apple_token = token
                    instance.save()
                    user = User.objects.get(id=instance.id)
                    token = jwt_encode(user)
                    data = {
                        'user': user,
                        'token': token
                    }
                    serializer = JWTSerializer(instance=data)
                    return Response({
                        "status": "OK",
                        "message": success_message,
                        "data": serializer.data
                    })

        except Exception as inst:
            print(inst)
            return Response({
                "status": "FAIL",
                "message": unsuccess_message,
                "data": []
            })
