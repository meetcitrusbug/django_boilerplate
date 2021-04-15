from . import views
from django.urls import path


urlpatterns = [
    path('product-list/',views.ProductListViewAPI.as_view(), name="product-list-api"),
    path('product-details/<int:id>',views.PorductDetailsAPIView.as_view(), name="product-details-api"),
    path('product/create',views.PrductCreateAPIView.as_view(), name="product-create-api"),
    path('product/update/<int:id>',views.ProductUpdateAPIView.as_view(), name="product-delete-api"),
    path('product/delete/<int:id>',views.ProductDeleteAPIView.as_view(), name="product-delete-api"),
    path('product-image/delete/<int:id>',views.ProductImageDeleteAPIView.as_view(), name="product-image-api"),
]
