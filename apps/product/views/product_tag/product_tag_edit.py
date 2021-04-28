from django.views.generic import UpdateView
from product.models import ProductTag
from product.forms import AddProductTagForm
from django.shortcuts import reverse
from django_boilerplate.views.generic import MyNewFormsetUpdateView


class EditProductTagView(MyNewFormsetUpdateView):
    
    template_name = "product_tag/edit.html"
    form_class = AddProductTagForm
    model = ProductTag
