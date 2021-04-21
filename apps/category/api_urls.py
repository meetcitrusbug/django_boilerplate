from django.urls import path
from category import api_views


urlpatterns = [
    path('category/', api_views.CategoryListAPIView.as_view(), name="category-api-view"),
    path('add-category/', api_views.AddCategoryAPIView.as_view(), name="add-category-api-view"),
    path('edit-category/<int:id>', api_views.EditCategoryAPIView.as_view(), name="edit-category-api-view"),
    path('delete-category/<int:id>', api_views.DeleteCategoryAPIView.as_view(), name="delete-category-api-view"),
        
    path('sub-category/', api_views.SubCategoryListAPIView.as_view(), name="subcategory-api-view"),
    path('add-subcategory/', api_views.AddSubCategoryAPIView.as_view(), name="add-subcategory-api-view"),
    path('edit-subcategory/<int:id>', api_views.EditSubCategoryAPIView.as_view(), name="edit-subcategory-api-view"),
    path('delete-subcategory/<int:id>', api_views.DeleteSubCategoryAPIView.as_view(), name="delete-subcategory-api-view"),
]