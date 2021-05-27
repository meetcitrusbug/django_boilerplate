from order.api_views import (OrderPlaceAPIView, GenerateStripeCartToken, PlaceOrderWithCardAPIView, CardListAPIView,
                            CardDeleteAPIView, OrderListAPIView, OrderStatusUpdateAPIView, OrderDetailsAPIView, CardAddAPIView)
from django.urls import path

urlpatterns = [
    path('place-order', OrderPlaceAPIView.as_view(), name='place-order-api'),
    path('place/order/with/card', PlaceOrderWithCardAPIView.as_view(), name='place-order-with-card-api'),
    
    path('card/list', CardListAPIView.as_view(), name='card-list-api'),   
    path('card/add/', CardAddAPIView.as_view(), name='card-add-api'),
    path('card/delete/<int:pk>', CardDeleteAPIView.as_view(), name='card-delete-api'),
    
    path('order/list/', OrderListAPIView.as_view(), name='order-list-api'),
    path('order-status-update/<int:pk>', OrderStatusUpdateAPIView.as_view(), name='order-status-update-api'),
    path('order/details/<int:pk>', OrderDetailsAPIView.as_view(), name='order-details-api'),
    
    path('stripe/card/token', GenerateStripeCartToken.as_view(), name='stripe-card-token-api'),
]