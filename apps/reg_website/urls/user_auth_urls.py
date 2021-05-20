from django.urls import path, include
from .. import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('sign-up/', views.SignUpView.as_view(), name='signup'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('email-login/', views.SignInView.as_view(), name='email_login'),
    path('otp-login/',views.LoginWithOTPView.as_view(), name='otp_login'),
    path('logout/', login_required(views.logoutView), name='logout'),
    path('forgot-password/', views.ForgotPasswordView.as_view(), name='forgot_password'),
    path('reset-password/<str:uid>/', views.ResetPasswordView.as_view(), name='password_reset'),
    path('verify-email/<str:uuid>/', views.EmailVerificationView.as_view(), name='verify'),
    path('verify-phone/', views.verifyPhoneView, name='verify_phone'),
    path('send-otp-verification/', views.sendOTPRegister, name='send_otp_verification'),
    path('send-login-otp/', views.sendOTPLogin, name='send_login_otp'),
]
