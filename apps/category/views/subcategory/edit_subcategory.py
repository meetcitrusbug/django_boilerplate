from django.views.generic import UpdateView
from category.forms import AddSubCategoryForm
from category.models import SubCategory
from django.shortcuts import reverse

class SubCategoryEditView(UpdateView):
    
    model = SubCategory
    form_class = AddSubCategoryForm
    template_name = 'subcategory/subcategory_edit.html'
    permission_required = ("edit_subcategory",)
    
    def get_context_data(self, **kwargs):
        context = super(SubCategoryEditView, self).get_context_data(**kwargs)
        context['model_name'] = self.model._meta.model_name
        return context
    
    def get_success_url(self):
        return reverse('subcategory-list')