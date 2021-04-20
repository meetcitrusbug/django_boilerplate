from django.urls import path
from . import views


urlpatterns = [
    path("", views.CategoryListView.as_view(), name="category-list"),
    path("category-ajax", views.CategoryDataTablesAjaxPagination.as_view(), name="category-list-ajax"),
    path("add-category/", views.CategoryAddView.as_view(), name="add-category"),
    path("edit-category/<int:pk>", views.CategoryEditView.as_view(), name="edit-category"),
    path("delete-category/<int:pk>", views.CategoryDeleteView.as_view(), name="delete-category"),
]