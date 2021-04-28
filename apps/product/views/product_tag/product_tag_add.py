from django.views.generic import CreateView
from product.models import ProductTag
from product.forms import AddProductTagForm
from django.shortcuts import reverse
from django_boilerplate.views.generic import MyNewFormsetCreateView

class AddProductTagView(MyNewFormsetCreateView):
    
    template_name="product_tag/add.html"
    model = ProductTag
    form_class= AddProductTagForm