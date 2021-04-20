from django.views.generic import CreateView
from category.forms import AddSubCategoryForm
from category.models import SubCategory
from django.shortcuts import reverse

class SubCategoryAddView(CreateView):
    
    model = SubCategory
    form_class = AddSubCategoryForm
    template_name = 'subcategory/subcategory_add.html'
    permission_required = ("add_subcategory",)
    
    def get_context_data(self):
        context = super(SubCategoryAddView, self).get_context_data()
        context['model_name'] = self.model._meta.model_name
        return context
    
    def get_success_url(self):
        return reverse('subcategory-list')