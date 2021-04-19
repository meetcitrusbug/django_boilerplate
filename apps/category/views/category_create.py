from django.views.generic import CreateView
from category.forms import AddCategoryForm
from category.models import Category
from django.shortcuts import reverse

class CategoryAddViewAPI(CreateView):
    
    model = Category
    form_class = AddCategoryForm
    template_name = 'category_add.html'
    permission_required = ("core.add_category",)
    
    def get_context_data(self):
        context = super(CategoryAddViewAPI, self).get_context_data()
        context['model_name'] = self.model._meta.model_name
        return context
    
    def get_success_url(self):
        return reverse('category-list')