from product.models import Product, ProductImage, ProductTag
from django.views.generic import  CreateView
from product.forms import AddProductForm, ProductTagFormset, ProductImageFormset
from django.shortcuts import reverse, redirect
from django_boilerplate.views.generic import MyNewFormsetCreateView

class AddProductView(MyNewFormsetCreateView):
    
    model = Product
    inline_model = ProductTag
    inlines = [ProductTagFormset, ProductImageFormset]
    form_class = AddProductForm
    template_name = 'add_product.html'
    permission_required = ("add_product",)
    