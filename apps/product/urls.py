from . import views
from django.urls import path

urlpatterns = [
        path('', views.ProductListView.as_view(), name="product-list"),
        path('product-ajax', views.DataTablesAjaxPagination.as_view(), name='product-list-ajax'),
        path('add-product/', views.AddProductView.as_view(), name='add-product'),
        path('edit-product/<int:pk>', views.EditProductView.as_view(), name='edit-product'),
        path('delete-product/<int:pk>', views.DeleteProductView.as_view(), name='delete-product'),
        
        path('image/', views.ProductImageListView.as_view(), name='product-image'),
        path('image-ajax/', views.ProductImageDataTablesAjaxPagination.as_view(), name='productimage-list-ajax'),
        path('image/add', views.AddProductImageView.as_view(), name='add-productimage'),
        path('image/edit/<int:pk>', views.EditProducImageView.as_view(), name='edit-productimage'),
        path('image/delete/<int:pk>', views.ProductImageDeleteView.as_view(), name='delete-productimage'),
        
        path('tag/', views.ProdcutTagListView.as_view(), name='product-tag'),
        path('tag-ajax/', views.ProductTagDataTablesAjaxPagination.as_view(), name='producttag-list-ajax'),
        path('tag/add', views.AddProductTagView.as_view(), name='add-producttag'),
        path('tag/edit/<int:pk>', views.EditProductTagView.as_view(), name='edit-producttag'),
        path('tag/delete/<int:pk>', views.DeleteProdcutTagView.as_view(), name='delete-producttag'),
        
    ]