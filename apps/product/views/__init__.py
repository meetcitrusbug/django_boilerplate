from .product_list import ProductListView, DataTablesAjaxPagination
from . add_product import AddProductView
from .edit_product import EditProductView
from .delete_product import DeleteProductView   

from .product_image.product_image_list import ProductImageListView, ProductImageDataTablesAjaxPagination
from .product_image.product_image_add import AddProductImageView
from .product_image.product_image_edit import EditProducImageView
from .product_image.product_image_delete import ProductImageDeleteView

from .product_tag.product_tag_list import ProdcutTagListView, ProductTagDataTablesAjaxPagination
from .product_tag.product_tag_add import AddProductTagView
from .product_tag.product_tag_edit import EditProductTagView
from .product_tag.product_tag_delete import DeleteProdcutTagView


from .products import ProductView
from .product_details import ProductDetails