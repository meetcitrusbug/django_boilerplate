from django.urls import  path, include

urlpatterns = [
    path("", include('category.api_urls')),
    path("", include('product.api_urls')),
]