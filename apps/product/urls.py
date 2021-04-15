from . import views
from django.urls import path


urlpatterns = [
    path('product-list/',views.ProductListViewAPI.as_view(), name="product-list-api"),
    path('product-details/<int:id>',views.PorductDetailsAPIView.as_view(), name="product-details-api"),
]
