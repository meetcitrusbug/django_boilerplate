from django.views.generic import UpdateView
from product.forms import AddProductImageForm
from product.models import ProductImage
from django.shortcuts import reverse
from django_boilerplate.views.generic import MyNewFormsetUpdateView

class EditProducImageView(MyNewFormsetUpdateView):
    
    model = ProductImage
    form_class = AddProductImageForm
    template_name = 'product_image/edit.html'
    permission_required = ("edit_category",)