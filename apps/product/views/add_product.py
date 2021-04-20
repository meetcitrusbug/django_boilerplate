from product.models import Product, ProductImage
from django.views.generic import  CreateView
from product.forms import AddProductForm, ProductTagFormset, ProductImageFormset
from django.shortcuts import reverse, redirect

class AddProductView(CreateView):
    
    model = Product
    form_class = AddProductForm
    formset = ProductTagFormset
    template_name = 'add_product.html'
    permission_required = ("add_product",)
    
    def get_context_data(self):
        context = super(AddProductView, self).get_context_data()
        context['model_name'] = self.model._meta.model_name
        context['formset'] = self.formset
        return context
    
    def form_valid(self, form):
        product = form.save(commit=False)
        print('====================>>>',self.request.POST)
        return redirect(self.get_success_url())
    
    def get_success_url(self):
        """Get success URL"""
        return reverse("product-list")
    