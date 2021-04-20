from product.models import Product, ProductImage
from django.views.generic import  DeleteView
from product.forms import AddProductForm
from django.urls import reverse

class DeleteProductView(DeleteView):
    
    model = Product
    form_class = AddProductForm
    template_name = 'delete_product.html'
    permission_required = ("delete_product",)
    
    def get_context_data(self, object):
        context = super(DeleteProductView, self).get_context_data(object=object)
        context['model_name'] = self.model._meta.model_name
        return context
    
    def get_success_url(self):
        """Get success URL"""
        return reverse("product-list")
    