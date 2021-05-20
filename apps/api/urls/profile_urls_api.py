from django.urls import path
from .. import views

urlpatterns = [
    path('profile/',views.ChangeProfileAPIView.as_view(),name='profile_view'),
    path('change-password/',views.ChangePasswordAPIVIew.as_view(),name='change_password')
]