from django.shortcuts import render
from django.views import View
from product.models import Product, ProductImage

class ProductDetails(View):
    
    template_name = "product_details.html"
    model = Product
    kwargs = {}
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())
    
    def get_context_data(self):
        self.kwargs['product'] = self.get_object(self.kwargs.get('pk'))
        self.kwargs['images'] = self.get_images(self.kwargs.get('pk'))
        return  self.kwargs

    def get_object(self, pk):
        try:
            return self.model.objects.get(pk=pk)
        except self.model.DoesNotExist:
            return None
        
    def get_images(self, pk):
        return ProductImage.objects.filter(product__pk=pk).order_by('id')