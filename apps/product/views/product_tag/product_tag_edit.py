from django.views.generic import UpdateView
from product.models import ProductTag
from product.forms import AddProductTagForm
from django.shortcuts import reverse


class EditProductTagView(UpdateView):
    
    template_name = "product_tag/edit.html"
    form_class = AddProductTagForm
    model = ProductTag
    
    
    def get_context_data(self):
        kwargs = super(EditProductTagView, self).get_context_data()
        kwargs['model_name'] = self.model._meta.model_name
        return kwargs
    
    def get_success_url(self):
        return reverse('product-tag')