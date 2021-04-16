from product.models import Product, ProductImage
from django.views.generic import  UpdateView
from product.forms import AddProductForm
from django.urls import reverse

class EditProductView(UpdateView):
    
    model = Product
    form_class = AddProductForm
    template_name = 'edit_product.html'
    permission_required = ("core.edit_product",)
    
    def get_context_data(self):
        context = super(EditProductView, self).get_context_data()
        context['model_name'] = self.model._meta.model_name
        return context
    
    def get_success_message(self):
        """Get success message"""
        print("================priting message=-=-=-=-=-=-=-=-=-")
        return "{0} save successfully".format(self.model._meta.model_name)
    
    def get_success_url(self):
        """Get success URL"""
        return reverse("product-list")
    