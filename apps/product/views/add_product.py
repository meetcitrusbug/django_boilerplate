from product.models import Product, ProductImage
from django.views.generic import  CreateView
from product.forms import AddProductForm, ProductTagFormset, ProductImageFormset
from django.shortcuts import reverse, redirect
from django_boilerplate.views.generic import MyNewFormsetCreateView

class AddProductView(MyNewFormsetCreateView):
    
    model = Product
    form_class = AddProductForm
    formset = ProductTagFormset
    template_name = 'add_product.html'
    permission_required = ("add_product",)
    
    # def get_success_url(self):
    #     """Get success URL"""
    #     return reverse("product-list")
