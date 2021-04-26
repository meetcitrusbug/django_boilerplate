from django.views.generic import UpdateView
from product.forms import AddProductImageForm
from product.models import ProductImage
from django.shortcuts import reverse

class EditProducImageView(UpdateView):
    
    model = ProductImage
    form_class = AddProductImageForm
    template_name = 'product_image/edit.html'
    permission_required = ("edit_category",)
    
    def get_context_data(self):
        context = super(EditProducImageView, self).get_context_data()
        context['model_name'] = self.model._meta.model_name
        return context
    
    def get_success_url(self):
        """Get success URL"""
        return reverse("product-image")