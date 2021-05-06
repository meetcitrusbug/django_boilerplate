from django.urls import path
from cart.api_views import (CartListAPIView, AddItemsAPIView, RemoveItemsAPIView,
                            RemoveAllItemsAPIView)

urlpatterns = [
    path('cart-list/', CartListAPIView.as_view(), name="cart-list-api"),
    path('cart-add-items/', AddItemsAPIView.as_view(), name="cart-add-items-api"),
    path('cart-remove-items/', RemoveItemsAPIView.as_view(), name="remove-items-api"),
    path('cart-remove-all-items/', RemoveAllItemsAPIView.as_view(), name="remove-all-items-api"),
]