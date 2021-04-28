from django.views.generic import  DeleteView
from category.models import Category
from category.forms import AddCategoryForm
from django.shortcuts import reverse
from django_boilerplate.views.generic import (
    MyDeleteView,
)

class CategoryDeleteView(MyDeleteView):
    
    model = Category
    form_class = AddCategoryForm
    template_name = "confirm_delete.html"
    permission_required = ("delete_product")
    
    
    def get_context_data(self, object):
        context = super(CategoryDeleteView, self).get_context_data(object=object)
        context['model_name'] = self.model._meta.model_name
        return context
    
    def get_success_url(self):
        """Get success URL"""
        return reverse("category-list")