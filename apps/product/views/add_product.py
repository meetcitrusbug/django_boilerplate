from product.models import Product, ProductImage
from django.views.generic import  CreateView
from product.forms import AddProductForm
from django.urls import reverse

class AddProductView(CreateView):
    
    model = Product
    form_class = AddProductForm
    template_name = 'add_product.html'
    permission_required = ("core.add_product",)
    
    def get_context_data(self):
        context = super(AddProductView, self).get_context_data()
        context['model_name'] = self.model._meta.model_name
        return context
    
    def get_success_url(self):
        """Get success URL"""
        return reverse("product-list")
    