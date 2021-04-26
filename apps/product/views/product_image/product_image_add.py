from product.models import Product, ProductImage
from django.views.generic import  CreateView
from product.forms import AddProductImageForm
from django.shortcuts import reverse, redirect

class AddProductImageView(CreateView):
    
    model = ProductImage
    form_class = AddProductImageForm
    template_name = 'product_image/add.html'
    permission_required = ("add_productimage",)
    
    def get_context_data(self):
        context = super(AddProductImageView, self).get_context_data()
        context['model_name'] = self.model._meta.model_name
        return context
    
    # def form_valid(self, form):
    #     print("===========================", self.request.POST)
    #     product = form.save(commit=False)
    #     return redirect(self.get_success_url())
    
    def get_success_url(self):
        """Get success URL"""
        return reverse("product-image")
    