from django.urls import path
from . import views


urlpatterns = [
    path("", views.CategoryListView.as_view(), name="category-list"),
    path("category-ajax", views.CategoryDataTablesAjaxPagination.as_view(), name="category-list-ajax"),
    path("add-category/", views.CategoryAddViewAPI.as_view(), name="add-category"),
]