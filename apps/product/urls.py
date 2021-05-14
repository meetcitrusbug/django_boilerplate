from . import views
from django.urls import path

urlpatterns = [       
        
        path('', views.ProductView.as_view(), name='products'),
        path('', views.ProductView.as_view(), name='index'),
        path('details/<int:pk>', views.ProductDetails.as_view(), name='product-details'),
    ]