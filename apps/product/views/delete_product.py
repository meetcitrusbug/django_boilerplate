from product.models import Product, ProductImage
from django.views.generic import  DeleteView
from product.forms import AddProductForm
from django.urls import reverse
from django_boilerplate.views.generic import MyDeleteView

class DeleteProductView(MyDeleteView):
    
    model = Product
    form_class = AddProductForm
    template_name = 'confirm_delete.html'
    permission_required = ("delete_product",)