from django.views.generic import UpdateView
from category.forms import AddCategoryForm
from category.models import Category
from django.shortcuts import reverse

class CategoryEditView(UpdateView):
    
    model = Category
    form_class = AddCategoryForm
    template_name = 'category_edit.html'
    permission_required = ("edit_category",)
    
    def get_context_data(self):
        context = super(CategoryEditView, self).get_context_data()
        context['model_name'] = self.model._meta.model_name
        return context
    
    def get_success_url(self):
        return reverse('category-list')