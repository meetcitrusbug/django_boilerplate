from django.urls import path
from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("login/", views.LoginPageView.as_view(), name="login"),
    path('userlogout/', views.userlogout, name='userlogout'),
    path('read/<int:pk>/', views.UserReadView.as_view(), name='read'),
    path('readall/', views.UserReadAllView.as_view(), name='readall'),
    path('remove/<int:pk>/', views.UserRemoveView.as_view(), name='remove'),
    path('removeall/', views.UserRemoveAllView.as_view(), name='removeall'),
]