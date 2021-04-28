from product.models import Product, ProductImage
from django.views.generic import  CreateView
from product.forms import AddProductImageForm
from django.shortcuts import reverse, redirect
from django_boilerplate.views.generic import MyNewFormsetCreateView

class AddProductImageView(MyNewFormsetCreateView):
    
    model = ProductImage
    form_class = AddProductImageForm
    template_name = 'product_image/add.html'
    permission_required = ("add_productimage",)
