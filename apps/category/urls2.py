from django.urls import path
from . import views


urlpatterns = [   
    path("", views.SubCategoryListView.as_view(), name="subcategory-list"),
    path("subcategory-ajax", views.SubCategoryDataTablesAjaxPagination.as_view(), name="subcategory-list-ajax"),
    path("add-subcategory/", views.SubCategoryAddView.as_view(), name="subcategory-create"),
    path("edit-subcategory/<int:pk>", views.SubCategoryEditView.as_view(), name="subcategory-update"),
    path("delete-subcategory/<int:pk>", views.SubCategoryDeleteView.as_view(), name="subcategory-delete"),
]