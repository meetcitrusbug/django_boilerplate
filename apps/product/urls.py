from . import views
from django.urls import path

urlpatterns = [
        path('list/', views.ProductListView.as_view(), name="product-list"),
        path('product-ajax', views.DataTablesAjaxPagination.as_view(), name='product-list-ajax'),
        path('add-product/', views.AddProductView.as_view(), name='product-create'),
        path('edit-product/<int:pk>', views.EditProductView.as_view(), name='product-update'),
        path('delete-product/<int:pk>', views.DeleteProductView.as_view(), name='product-delete'),
        
        path('image/', views.ProductImageListView.as_view(), name='productimage-list'),
        path('image-ajax/', views.ProductImageDataTablesAjaxPagination.as_view(), name='productimage-list-ajax'),
        path('image/add', views.AddProductImageView.as_view(), name='productimage-create'),
        path('image/edit/<int:pk>', views.EditProducImageView.as_view(), name='productimage-update'),
        path('image/delete/<int:pk>', views.ProductImageDeleteView.as_view(), name='productimage-delete'),
        
        path('tag/', views.ProdcutTagListView.as_view(), name='producttag-list'),
        path('tag-ajax/', views.ProductTagDataTablesAjaxPagination.as_view(), name='producttag-list-ajax'),
        path('tag/add', views.AddProductTagView.as_view(), name='producttag-create'),
        path('tag/edit/<int:pk>', views.EditProductTagView.as_view(), name='producttag-update'),
        path('tag/delete/<int:pk>', views.DeleteProdcutTagView.as_view(), name='producttag-delete'),
        
        
        path('tag/delete/<int:pk>', views.DeleteProdcutTagView.as_view(), name='delete-producttag'),
        
        
        path('', views.ProductView.as_view(), name='products'),
        path('details/<int:pk>', views.ProductDetails.as_view(), name='product-details'),
    ]