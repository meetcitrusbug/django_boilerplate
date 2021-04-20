from django.views.generic import  DeleteView
from category.models import SubCategory
from category.forms import AddSubCategoryForm
from django.shortcuts import reverse

class SubCategoryDeleteView(DeleteView):
    
    model = SubCategory
    form_class = AddSubCategoryForm
    template_name = "subcategory/subcategory_delete.html"
    permission_required = ("delete_subcategory")
    
    
    def get_context_data(self, object):
        context = super(SubCategoryDeleteView, self).get_context_data(object=object)
        context['model_name'] = self.model._meta.model_name
        return context
    
    def get_success_url(self):
        """Get success URL"""
        return reverse("subcategory-list")