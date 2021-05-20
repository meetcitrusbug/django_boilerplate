from django.urls import path, include
from .. import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
        path('profile/',login_required(views.ChangeProfileView.as_view(),login_url='reg_website:email_login'),name='profile_view'),
        path('change-password/',login_required(views.ChangePasswordView.as_view(),login_url='reg_website:email_login'),name='change_password')
 ]