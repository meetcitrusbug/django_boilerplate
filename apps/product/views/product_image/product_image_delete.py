from django.views.generic import  DeleteView
from product.models import ProductImage
# from category.forms import AddCategoryForm
from django.shortcuts import reverse

class ProductImageDeleteView(DeleteView):
    
    model = ProductImage
    # form_class = AddCategoryForm
    template_name = "product_image/delete.html"
    permission_required = ("delete_productimage")
    
    
    def get_context_data(self, object):
        context = super(ProductImageDeleteView, self).get_context_data(object=object)
        context['model_name'] = self.model._meta.model_name
        return context
    
    def get_success_url(self):
        """Get success URL"""
        return reverse("product-image")