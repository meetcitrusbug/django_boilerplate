from django.views.generic import DeleteView
from product.models import ProductTag
from django.shortcuts import reverse

class DeleteProdcutTagView(DeleteView):
    
    model = ProductTag
    queryset = model.objects.all()
    template_name = "product_tag/delete.html"
    
    
    def get_context_data(self, object):
        kwargs = super(DeleteProdcutTagView, self).get_context_data(object=object)
        kwargs['model_name'] = self.model._meta.model_name
        return kwargs
    
    def get_success_url(self):
        return reverse('product-tag')