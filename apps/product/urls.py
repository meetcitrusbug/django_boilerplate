from . import views
from django.urls import path

urlpatterns = [
        path('', views.ProductListView.as_view(), name="product-list"),
        path('product-ajax', views.DataTablesAjaxPagination.as_view(), name='product-list-ajax'),
        path('add-product/', views.AddProductView.as_view(), name='add-product'),
        path('edit-product/<int:pk>', views.EditProductView.as_view(), name='edit-product'),
        path('delete-product/<int:pk>', views.DeleteProductView.as_view(), name='delete-product'),
    ]