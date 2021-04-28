from django.views.generic import DeleteView
from product.models import ProductTag
from django.shortcuts import reverse
from django_boilerplate.views.generic import MyDeleteView

class DeleteProdcutTagView(MyDeleteView):
    
    model = ProductTag
    queryset = model.objects.all()
    template_name = "confirm_delete.html"
    
    
    def get_context_data(self, object):
        kwargs = super(DeleteProdcutTagView, self).get_context_data(object=object)
        kwargs['model_name'] = self.model._meta.model_name
        return kwargs