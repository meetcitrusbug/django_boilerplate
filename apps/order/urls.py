from django.urls import path

from order.views import (OrderListView, DataTablesAjaxPagination, OrderDetailsAPIView, OrderDetailsAPIView, CheckoutDetailsView,
                         OrdersList, CheckoutWithCardView, CardsList, CardDeletView, AddCardView, OrderDetailsView, CardDefaultView)
customadmin = 'customadmin/'

urlpatterns = [
    path('%sorder-list/' % customadmin , OrderListView.as_view(), name="order-list"),
    path('%sorder-list-ajax/'% customadmin, DataTablesAjaxPagination.as_view(), name="order-list-ajax"),
    path('%sorder-details/<int:pk>' % customadmin, OrderDetailsAPIView.as_view(), name="order-details"),
    path('checkout/', CheckoutDetailsView.as_view(), name="checkout"),
    path('checkout-card/', CheckoutWithCardView.as_view(), name="checkout-card"),
    path('orders/', OrdersList.as_view(), name="orders"),
    path('order/details/<int:pk>', OrderDetailsView.as_view(), name="order-detail"),
    path('cards/', CardsList.as_view(), name="cards"),
    path('card/delete/<int:pk>', CardDeletView.as_view(), name="card-delete"),
    path('card/add/', AddCardView.as_view(), name="card-add"),
    path('card/default/<int:pk>', CardDefaultView.as_view(), name="card-default"),
]