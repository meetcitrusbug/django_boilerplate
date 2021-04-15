from django.urls import path
from category import api_views


urlpatterns = [
    path('category/', api_views.CategoryListAPIView.as_view(), name="category-api-view"),
    path('sub-category/', api_views.SubCategoryListAPIView.as_view(), name="subcategory-api-view"),
]