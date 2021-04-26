from django.views.generic import CreateView
from product.models import ProductTag
from product.forms import AddProductTagForm
from django.shortcuts import reverse

class AddProductTagView(CreateView):
    
    template_name="product_tag/add.html"
    model = ProductTag
    form_class= AddProductTagForm
    
    
    def get_context_data(self):
        context = super(AddProductTagView, self).get_context_data()
        context['model_name'] = self.model._meta.model_name
        return context
    
    def get_success_url(self):
        return reverse('product-tag')