from django.urls import  path, include

urlpatterns = [
    path("", include('category.urls')),
    path("", include('product.urls')),
]