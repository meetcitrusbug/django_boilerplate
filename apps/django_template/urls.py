from django.urls import path
from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("login/", views.LoginPageView.as_view(), name="login"),
    path('userlogout/', views.userlogout, name='userlogout'),
    path('cards/', views.CardsList.as_view(), name="cards"),
    path('card/delete/<int:pk>', views.CardDeletView.as_view(), name="card-delete"),
    path('card/add/', views.AddCardView.as_view(), name="card-add"),
    path('checkout-card/<int:pk>', views.CheckoutWithCardView.as_view(), name="checkout-card"),
    path('cancel-subscription/', views.CancelSubscriptionView.as_view(), name="cancel-subscription"),
]