from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views import View
from django.contrib.sites.shortcuts import get_current_site
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.cache import cache_control


from django_boilerplate.helpers import send_email
from django_boilerplate import settings

import uuid

from twilio.rest import Client

from ..forms import SignUpForm
from ..models import User

import random
import hashlib


class SignUpView(TemplateView):
    template_name = 'auth_user_templates/registration.html'
    form = SignUpForm

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            context = {'Title': "Sign Up", 'form': self.form}
            return render(request, self.template_name, context)
        return redirect('reg_website:profile_view')


class RegisterView(View):
    def post(self, request):
        current_site = f'http://{get_current_site(request)}/verify-email/'
        email = request.POST.get('email')
        email_exists = User.objects.filter(email=email)
        if email_exists:
            response = {
                "message": "Email already exits.",
                "status": False
            }
            return JsonResponse(response)
        username = request.POST.get('username')
        username_exists = User.objects.filter(username=username)
        if username_exists:
            response = {
                "message": "Username already exits.",
                "status": False
            }
            return JsonResponse(response)

        phone_number = request.POST.get('phone')
        phone_exists = User.objects.filter(phone=phone_number)
        if phone_exists:
            response = {
                "message": "Phone Number already exits.",
                "status": False
            }
            return JsonResponse(response)
        if phone_number[0] == '-':
            response = {
                "message": "Enter valid phone number.",
                "status": False
            }
            return JsonResponse(response)
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        user = User(email=email, username=username, first_name=first_name,last_name=last_name, phone=phone_number)
        user.set_password(password)
        user.phone_verified = True
        user.save()
        subject = "Email verification"
        text_content = f"Hello, \nPlease click the below link to verify your email. \n {current_site}{user.unique_id}/"
        send_email(user, subject, text_content)
        response = {
            "message": "User Registered Successfully.",
            "status": True
        }
        return JsonResponse(response)


def sendOTPRegister(request):
    phone = request.GET.get('phone')
    if not phone:
        response = {
            "message": "Phone Is required.",
            "status": False
        }
        return JsonResponse(response)
    user = User.objects.filter(phone=phone)
    if user:
        response = {
            "message": "User With this phone number already exists.",
            "status": False
        }
        return JsonResponse(response)
    if phone[0] == '-':
        response = {
            "message": "Enter valid phone number.",
            "status": False
        }
        return JsonResponse(response)
    phone_no = '+91' + phone
    OTP = random.randint(000000, 999999)
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    client.messages.create(body=f"Your OTP for Verification is {OTP}", from_=settings.TWILIO_MOBILE,
                           to=phone_no)
    hash_otp = hashlib.sha256(str(OTP).encode())
    request.session['otp'] = hash_otp.hexdigest()
    response = {
        "message": "OTP sent successfully.",
        "status": True
    }
    return JsonResponse(response)


def verifyPhoneView(request):
    OTP = request.GET.get('otp')
    hash_otp = hashlib.sha256(str(OTP).encode())
    hex_otp = hash_otp.hexdigest()
    if hex_otp==request.session.get('otp'):
        response = {
            "message": "OTP Verified successfully.",
            "status": True,
            "verified":True
        }
        return JsonResponse(response)
    response = {
        "message": "OTP verification unsuccessful.",
        "status": False,
        "verified":False
    }
    return JsonResponse(response)


class SignInView(TemplateView):
    template_name = 'auth_user_templates/login.html'

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            context = {'Title': "Sign In"}
            return render(request, self.template_name, context)
        return redirect('reg_website:profile_view')

    def post(self, request, *args, **kwargs):
        email_or_username = request.POST.get('email_or_username')
        password = request.POST.get('password')
        user = User.objects.filter(email=email_or_username)
        if not user:
            user = User.objects.filter(username=email_or_username)
        if user:
            if user[0].email_verified:
                account = authenticate(email=user[0].email,password=password)
                if account:
                    login(request, account)
                    response = {
                        "message": "Login successfully.",
                        "status": True
                    }
                    return JsonResponse(response)
                else:
                    response = {
                        "message": "Email/Username or Password combination invalid.",
                        "status": False
                    }
                    return JsonResponse(response)
            else:
                response = {
                    "message": "Email Is Not Verified.",
                    "status": False
                }
                return JsonResponse(response)
        else:
            response = {
                "message": "User not Exist.",
                "status": False
            }
            return JsonResponse(response)


class LoginWithOTPView(TemplateView):
    template_name = "auth_user_templates/login-with-otp.html"

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            context = {'Title': 'Login OTP'}
            return render(request, self.template_name, context)
        return redirect('reg_website:profile_view')

    def post(self, request):
        phone = request.POST.get('phone', None)
        otp = request.POST.get('OTP', None)
        user = User.objects.filter(phone=phone)
        if user:
            if otp!=user[0].otp_number:
                response = {
                    "message": "Wrong OTP Was Given.",
                    "status": False
                }
                return JsonResponse(response)

            user_auth = User.objects.get(id=user[0].id)
            login(request, user_auth)
            user_auth.otp_number = None
            user_auth.save()
            response = {
                "message": "Login Success.",
                "status": True
            }
            return JsonResponse(response)

        else:
            response = {
                "message": "User Not Exists.",
                "status": False
            }
            return JsonResponse(response)


def sendOTPLogin(request):
    phone = request.GET.get('phone')
    if not phone:
        response = {
            "message": "Phone Is required.",
            "status": False
        }
        return JsonResponse(response)
    user = User.objects.filter(phone=phone)
    if user:
        if user[0].phone_verified:
            phone_no = '+91' + phone
            OTP = random.randint(000000, 999999)
            try:
                client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
                client.messages.create(body=f"Your OTP for login with project is {OTP}", from_=settings.TWILIO_MOBILE,
                                       to=phone_no)
                user[0].otp_number = OTP
                user[0].save()
                response = {
                    "message": "OTP sent successfully.",
                    "status": True
                }
                return JsonResponse(response)
            except:
                response = {
                    "message": "Can Not Send Message Internal error.",
                    "status": False
                }
                return JsonResponse(response)
        else:
            response = {
                "message": "Phone Number Is Not Verified.",
                "status": False
            }
            return JsonResponse(response)
    else:
        response = {
            "message": "Phone Number Is Not Registered.",
            "status": False
        }
        return JsonResponse(response)



class ForgotPasswordView(TemplateView):
    template_name = 'auth_user_templates/forgot-password.html'

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            context = {'Title': "Forgot Password"}
            return render(request, self.template_name, context)
        return redirect('reg_website:profile_view')

    def post(self, request):
        email = request.POST.get('email')
        user_exists = User.objects.filter(is_active=True, email=email, email_verified=True)
        if user_exists:
            user_exists[0].password_reset_link = uuid.uuid4()
            user_exists[0].save()
            current_site = f'http://{get_current_site(request)}/reset-password/'
            subject = "Password reset link"
            text_content = f"Hello, \nYou recently requested to reset your password for your account. Please click the below link to change your password. \n {current_site}{user_exists[0].password_reset_link}/"
            send_email(user_exists[0], subject, text_content)
            response = {
                "message": "Email with reset link sent successful.",
                "status": True
            }
            return JsonResponse(response)
        else:
            response = {
                "message": "User with this email not exists.",
                "status": False
            }
            return JsonResponse(response)


class ResetPasswordView(View):
    template_name = 'auth_user_templates/set-password.html'

    def get(self, request, uid):
        context = {"uid": uid}
        return render(request, self.template_name, context)

    def post(self, request,uid):
        password = request.POST.get('password')

        if not uid:
            response = {
                "message": "Id Was Not Given.",
                "status": False
            }
            return JsonResponse(response)

        user_exists = User.objects.filter(is_active=True, password_reset_link=uid)
        if user_exists:
            user_exists[0].set_password(password)
            user_exists[0].password_reset_link = None
            user_exists[0].save()
            response = {
                "message": "Password reset successful.",
                "status": True
            }
            return JsonResponse(response)
        response = {
            "message": "Not a valid Link.",
            "status": False
        }
        return JsonResponse(response)


class EmailVerificationView(TemplateView):
    template_name = "auth_user_templates/verify-email.html"

    def get(self, request, uuid):
        try:
            user = User.objects.filter(unique_id=uuid)
            if not user:
                message = "User not exists"
                return render(request, self.template_name, {'Title': 'Email Verification', 'status': False,'message':message})
            if user[0].email_verified:
                message = "Email Already Verified"
                return render(request, self.template_name, {'Title': 'Email Verification', 'status': True,'message':message})
            user[0].email_verified = True
            user[0].save()
            send_email(user[0], subject=f"WElCOME PROJECT TITLE",
                       text_content=f"WELCOME, YOU HAVE SUCCESSFULLY COMPLETED YOUR EMAIL VERIFICATION")
            message = "User Verified Successfully!!"
            return render(request, self.template_name, {'Title': 'Email Verification', 'status': True,'message':message})
        except:
            message = "Error"
            return render(request, self.template_name, {'Title': 'Email Verification', 'status': False,'message':message})


class ReSendVerificationEmailView(View):
    def get(self,request,*args,**kwargs):
        if not request.user.is_authenticated:
            return render(request,"auth_user_templates/resend-email.html")
        return redirect('reg_website:email_login')

    def post(self, request):
        current_site = f'http://{get_current_site(request)}/verify-email/'
        email = request.POST.get('email')
        user = User.objects.filter(email=email)
        if user:
            if user[0].email_verified:
                response = {
                    "message": "User Verified Already.",
                    "status": False
                }
                return JsonResponse(response)
            subject = "Email verification"
            text_content = f"Hello, \nPlease click the below link to verify your email. \n {current_site}{user[0].unique_id}/"
            send_email(user[0], subject, text_content)
            response = {
                "message": "Verification mail resend Successfully.",
                "status": True
            }
            return JsonResponse(response)
        else:
            response = {
                "message": "User Not Exists.",
                "status": False
            }
            return JsonResponse(response)


@cache_control(no_cache=True, must_revalidate=True)
def logoutView(request):
    logout(request)
    return redirect('reg_website:email_login')
