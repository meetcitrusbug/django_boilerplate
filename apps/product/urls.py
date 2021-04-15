from . import api_views
from django.urls import path


urlpatterns = [
    path('product-list/', api_views.ProductListViewAPI.as_view(), name="product-list-api"),
    path('product-details/<int:id>', api_views.PorductDetailsAPIView.as_view(), name="product-details-api"),
    path('product/create', api_views.PrductCreateAPIView.as_view(), name="product-create-api"),
    path('product/update/<int:id>' ,api_views.ProductUpdateAPIView.as_view(), name="product-delete-api"),
    path('product/delete/<int:id>', api_views.ProductDeleteAPIView.as_view(), name="product-delete-api"),
    path('product-image/delete/<int:id>', api_views.ProductImageDeleteAPIView.as_view(), name="product-image-api"),
]
