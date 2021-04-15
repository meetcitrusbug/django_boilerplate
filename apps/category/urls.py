from django.urls import path
from category import views


urlpatterns = [
    path('category/', views.CategoryListAPIView.as_view(), name="category-api-view"),
    path('sub-category/', views.SubCategoryListAPIView.as_view(), name="subcategory-api-view"),
]