from django.urls import path
from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("login/", views.LoginPageView.as_view(), name="login"),
    path('userlogout/', views.userlogout, name='userlogout'),
    path('detail/<int:pk>/', views.MediaCategoryDetailView.as_view(), name='detail'),
]