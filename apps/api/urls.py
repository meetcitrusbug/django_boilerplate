from django.urls import path
from . import views

urlpatterns = [
    path('rest-auth/facebook/', views.FacebookLogin.as_view(), name='fb_login'),
    path('rest-auth/google/', views.GoogleLogin.as_view(), name='google_login'),
    path('rest-auth/twitter/', views.TwitterLogin.as_view(), name='twitter_login'),
    path('rest-auth/apple/', views.AppleLoginAPIView.as_view(), name='apple_login'),
]