from django.urls import path
from . import views

urlpatterns = [
    path("registration/", views.RegistrationView.as_view(), name="registration"),
    path("login/", views.LoginPageView.as_view(), name="login"),
    path('logout/', views.userlogout, name='logout'),
]