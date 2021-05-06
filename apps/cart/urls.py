from django.urls import path
from .views import (AddItemView, CartListAPIView, CartItemRemoveView, RemoveAllCartItemView)


urlpatterns = [
        path('add-item/<int:pk>', AddItemView.as_view(), name="add-to-cart"),
        path('list/', CartListAPIView.as_view(), name="cart-list"),
        path('cart-remove/<int:pk>', CartItemRemoveView.as_view(), name='cart-remove'),
        path('cart-remove-all/', RemoveAllCartItemView.as_view(), name='cart-remove-all'),
]