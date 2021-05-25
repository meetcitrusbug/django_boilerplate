from rest_framework.views import APIView
from rest_framework import status

from django.contrib.auth import authenticate, login, logout
from django.contrib.sites.shortcuts import get_current_site

from django_boilerplate.helpers import custom_response, serialized_response, send_email
from django_boilerplate.permissions import IsAccountOwner

from ..serializers import UserRegisterSerializer, UserLoginSerializer
from reg_website.models import User

import random
import uuid

from datetime import timezone
import datetime

from twilio.rest import Client
from django_boilerplate import settings


class SignUpApiView(APIView):
    serializer_class = UserRegisterSerializer

    def post(self, request, *args, **kwargs):
        current_site = f'http://{get_current_site(request)}/verify-email/'
        if not 'username' in request.data:
            return custom_response(status_value=False, code=status.HTTP_400_BAD_REQUEST, message="Username is required")

        if not 'phone' in request.data:
            return custom_response(status_value=False, code=status.HTTP_400_BAD_REQUEST, message="Phone is required")

        if not 'email' in request.data:
            return custom_response(status_value=False, code=status.HTTP_400_BAD_REQUEST, message="Email is required")

        email = User.objects.filter(email=request.data['email']).distinct()
        if email.exists():
            message = "Email exists use new email"
            return custom_response(status_value=True, code=status.HTTP_400_BAD_REQUEST, message=message)

        user = User.objects.filter(username=request.data['username']).distinct()
        if user.exists():
            message = "Username exists use new username"
            return custom_response(status_value=True, code=status.HTTP_400_BAD_REQUEST, message=message)

        phone = User.objects.filter(phone=request.data['phone']).distinct()
        if phone.exists():
            message = "Phone exists use new phone number"
            return custom_response(status_value=True, code=status.HTTP_400_BAD_REQUEST, message=message)

        message = "User Registered Successfully check email and mobile for verification"
        serializer = self.serializer_class(data=request.data, context={'request': request})
        response_status, result, message = serialized_response(serializer, message)
        status_code = status.HTTP_201_CREATED if response_status else status.HTTP_400_BAD_REQUEST
        if status_code == 201:
            subject = "Email verification"
            account = User.objects.get(email=request.data['email'])
            text_content = f"Hello, \nPlease click the below link to verify your email. \n {current_site}{account.unique_id}/"
            send_email(account, subject, text_content)
            phone_no = '+91' + account.phone
            OTP = random.randint(000000, 999999)
            account.otp_number = OTP
            account.save()
            client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
            client.messages.create(body=f"Your OTP for verification is {OTP}", from_=settings.TWILIO_MOBILE,
                                   to=phone_no)
        return custom_response(status_value=response_status, code=status_code, message=message, result=result)


class SignInAPIView(APIView):
    serializer_class = UserLoginSerializer

    def post(self, request, format=None):
        email_or_username = request.data.get("email_or_username", None)
        password = request.data.get("password", None)
        if not email_or_username or not password:
            message = "email/username or password was not given"
            return custom_response(status_value=False, code=status.HTTP_400_BAD_REQUEST, message=message)
        user = User.objects.filter(email=email_or_username)
        if not user:
            user = User.objects.filter(username=email_or_username)
        if user:
            account = authenticate(email=user[0].email, password=password)
            if account:
                if account.email_verified:
                    login(request, account)
                    serializer = self.serializer_class(account, context={'request': request})
                    return custom_response(status_value=True, code=status.HTTP_200_OK, message="Login Successful",
                                           result=serializer.data)
                else:
                    return custom_response(status_value=False, code=status.HTTP_400_BAD_REQUEST, message="Email Is not verified")
            else:
                message = "Password invalid"
                return custom_response(status_value=False, code=status.HTTP_400_BAD_REQUEST, message=message)
        else:
            message = "User not exist"
            return custom_response(status_value=False, code=status.HTTP_400_BAD_REQUEST, message=message)


class SignInOTPAPIView(APIView):
    serializer_class = UserLoginSerializer

    def post(self, request, format=None):
        phone = request.data.get('phone', None)
        otp = request.data.get('otp', None)
        if not phone or not otp:
            message = "Phone number or OTP is required"
            return custom_response(status_value=False, code=status.HTTP_400_BAD_REQUEST, message=message)
        user = User.objects.filter(phone=phone)
        if user:
            if not user[0].phone_verified:
                message = "Phone number is not verified"
                return custom_response(status_value=False, code=status.HTTP_400_BAD_REQUEST, message=message)
            if otp != user[0].otp_number:
                message = "Fail"
                return custom_response(status_value=False, code=status.HTTP_400_BAD_REQUEST, message=message)
            current_time = datetime.datetime.now(timezone.utc)
            expire_time = user[0].otp_number_expire
            if expire_time:
                if current_time <= expire_time:
                    user_auth = User.objects.get(id=user[0].id)
                    login(request, user_auth)
                    user_auth.otp_number = None
                    user_auth.otp_number_expire = None
                    user_auth.save()
                    serialize = self.serializer_class(user_auth, context={'request': request})
                    return custom_response(status_value=True, code=status.HTTP_200_OK, message="Login Success",
                                           result=serialize.data)
            user[0].otp_number = None
            user[0].otp_number_expire = None
            user[0].save()
            message = "Not valid otp or OTP has been expired"
            return custom_response(status_value=False, code=status.HTTP_400_BAD_REQUEST, message=message)
        else:
            message = "Not Recognized User"
            return custom_response(status_value=False, code=status.HTTP_400_BAD_REQUEST, message=message)


class LogOutAPIView(APIView):
    permission_classes = (IsAccountOwner,)

    def post(self, request, format=None):
        logout(request)
        message = "Logout successful"
        return custom_response(status_value=True, code=status.HTTP_200_OK, message=message)


class ForgotPasswordAPIView(APIView):
    def get(self, request, format=None):
        current_site = f'http://{get_current_site(request)}/reset-password/'
        if "email" not in request.data.keys():
            message = "Email field is missing!"
            return custom_response(False, status.HTTP_400_BAD_REQUEST, message)
        try:
            user = User.objects.get(email=request.data['email'])
        except User.DoesNotExist:
            user = None
        if not user:
            message = "User not found!"
            return custom_response(False, status.HTTP_400_BAD_REQUEST, message)
        if user:
            user.password_reset_link = uuid.uuid4()
            user.password_reset_link_expire = datetime.datetime.now(tz=timezone.utc) + datetime.timedelta(minutes=5)
            user.save()
            subject = "Password reset link"
            text_content = f"Hello, \nYou recently requested to reset your password for your account. Please click the below link to change your password. \n {current_site}{user.password_reset_link}/"
            send_email(user, subject, text_content)
        message = "Email to change password sent successfully!"
        return custom_response(True, status.HTTP_200_OK, message)


class ResetPasswordAPIView(APIView):

    def post(self, request, uid):
        password = request.data.get('password',None)
        if not password:
            message = "Password Was Not Given."
            return custom_response(False, status.HTTP_400_BAD_REQUEST, message)

        if not uid:
            message="Id Was Not Given."
            return custom_response(False, status.HTTP_400_BAD_REQUEST, message)

        user_exists = User.objects.filter(is_active=True, password_reset_link=uid)
        if user_exists:
            time_expire = user_exists[0].password_reset_link_expire
            if time_expire:
                current_time = datetime.datetime.now(timezone.utc)
                if current_time <= time_expire:
                    user_exists[0].set_password(password)
                    user_exists[0].password_reset_link = None
                    user_exists[0].password_reset_link_expire = None
                    user_exists[0].save()
                    message="Password reset successful."
                    return custom_response(True, status.HTTP_200_OK, message)
            user_exists[0].password_reset_link = None
            user_exists[0].password_reset_link_expire = None
            user_exists[0].save()
            message = "Link has been expired."
            return custom_response(False, status.HTTP_400_BAD_REQUEST, message)
        message="Not a valid Link."
        return custom_response(False, status.HTTP_400_BAD_REQUEST, message)



class EmailVerificationAPIView(APIView):
    def post(self, request, uuid):
        try:
            user = User.objects.filter(unique_id=uuid)
            if not user:
                message = "Link Is Not Valid!!"
                return custom_response(False, status.HTTP_400_BAD_REQUEST, message)
            if user[0].email_verified:
                message = "User Already Verified!!"
                return custom_response(False, status.HTTP_400_BAD_REQUEST, message)
            user[0].email_verified = True
            user[0].save()
            send_email(user[0],subject=f"WElCOME PROJECT TITLE",text_content=f"WELCOME, YOU HAVE SUCCESSFULLY COMPLETED YOUR EMAIL VERIFICATION")
            message = "User Verified Successfully!!"
            return custom_response(True, status.HTTP_200_OK, message)
        except:
            message = "User Not Found"
            return custom_response(False, status.HTTP_400_BAD_REQUEST, message)


class PhoneVerificationAPIView(APIView):
    permission_classes = (IsAccountOwner, )
    def post(self, request):
        if request.user.phone_verified:
            message = "Phone already verified"
            return custom_response(False, status.HTTP_400_BAD_REQUEST, message)

        if "otp" in request.data:
            user = request.user
            otp = request.data['otp']
            if otp == user.otp_number:
                user.phone_verified = True
                user.otp_number = None
                user.save()
                message = "Verification successful"
                return custom_response(True, status.HTTP_200_OK, message)
            else:
                message = "OTP was not correct"
                return custom_response(False, status.HTTP_400_BAD_REQUEST, message)
        else:
            message = "OTP is required"
            return custom_response(False, status.HTTP_400_BAD_REQUEST, message)


class ResendEmailVerificationAPIView(APIView):
    def post(self, request):
        current_site = f'http://{get_current_site(request)}/verify-email/'
        if 'email' in request.data:
            user = User.objects.filter(email=request.data['email'])
            if user:
                if user[0].email_verified:
                    message = "Email Already Verified!!"
                    return custom_response(False, status.HTTP_400_BAD_REQUEST, message)
                subject = "Email verification"
                account = User.objects.filter(email=request.data['email'])
                text_content = f"Hello, \nPlease click the below link to verify your email. \n {current_site}{account[0].unique_id}/"
                send_email(account[0], subject, text_content)
                message = "Email Sent Successfully!!"
                return custom_response(True, status.HTTP_200_OK, message)
            else:
                message = "User Not Found!!"
                return custom_response(False, status.HTTP_400_BAD_REQUEST, message)
        else:
            message = "Email is required!!"
            return custom_response(False, status.HTTP_400_BAD_REQUEST, message)


class SendOTPAPIView(APIView):
    def get(self, request):
        if "phone" not in request.data.keys():
            message = "Phone is required!"
            return custom_response(False, status.HTTP_400_BAD_REQUEST, message)
        try:
            user = User.objects.get(phone=request.data['phone'])
        except User.DoesNotExist:
            user = None
        if not user:
            message = "User not found!"
            return custom_response(False, status.HTTP_400_BAD_REQUEST, message)
        if user:
            phone_no = '+91' + request.data['phone']
            OTP = random.randint(000000, 999999)
            user.otp_number = OTP
            user.otp_number_expire = datetime.datetime.now(timezone.utc) + datetime.timedelta(minutes=5)
            user.save()
            client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
            client.messages.create(body=f"Your OTP for login with project is {OTP}", from_=settings.TWILIO_MOBILE,
                                   to=phone_no)
        message = "OTP sent successfully!"
        return custom_response(True, status.HTTP_200_OK, message)
