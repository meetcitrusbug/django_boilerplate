from product.models import Product, ProductImage, ProductTag
from django.views.generic import  UpdateView
from product.forms import AddProductForm, ProductTagFormset, ProductImageFormset
from django.urls import reverse
from django_boilerplate.views.generic import MyNewFormsetUpdateView

class EditProductView(MyNewFormsetUpdateView):
    
    model = Product
    inline_model = ProductTag
    inlines = [ProductTagFormset, ProductImageFormset]
    form_class = AddProductForm
    template_name = 'edit_product.html'
    permission_required = ("edit_product",)