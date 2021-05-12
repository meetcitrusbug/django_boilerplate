from django.views.generic import  DeleteView
from product.models import ProductImage
from django.shortcuts import reverse
from django_boilerplate.views.generic import MyDeleteView

class ProductImageDeleteView(MyDeleteView):
    
    model = ProductImage
    template_name = "confirm_delete.html"
    permission_required = ("delete_productimage")