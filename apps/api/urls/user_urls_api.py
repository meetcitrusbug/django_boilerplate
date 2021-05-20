from django.urls import path
from .. import views

urlpatterns = [
    path("register/", views.SignUpApiView.as_view(), name="register"),
    path("email-login/", views.SignInAPIView.as_view(), name="email_login"),
    path("otp-login/",views.SignInOTPAPIView.as_view(), name="otp_login"),
    path("logout/", views.LogOutAPIView.as_view(), name="logout"),
    path("forgot-password/",views.ForgotPasswordAPIView.as_view(),name='forgot-password'),
    path("reset-password/<str:uid>/", views.ResetPasswordAPIView.as_view(), name='reset-password'),
    path("verify-email/<str:uuid>/", views.EmailVerificationAPIView.as_view(), name="verify_email"),
    path("verify-phone/", views.PhoneVerificationAPIView.as_view(), name="verify_phone"),
    path("resend-email/", views.ResendEmailVerificationAPIView.as_view(), name="resend_email_verification"),
    path("send-otp/",views.SendOTPAPIView.as_view(),name='send-otp')
]
