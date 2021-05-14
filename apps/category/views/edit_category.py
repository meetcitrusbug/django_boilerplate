from django.views.generic import UpdateView
from category.forms import AddCategoryForm, SubCategoryFormset
from category.models import Category, SubCategory
from django.shortcuts import reverse
from django_boilerplate.views.generic import (
    MyNewFormsetUpdateView,
)

class CategoryEditView(MyNewFormsetUpdateView):
    
    model = Category
    inline_model = SubCategory
    inlines = [SubCategoryFormset]
    form_class = AddCategoryForm
    template_name = 'category_edit.html'
    permission_required = ("edit_category",)
    
    # def get_context_data(self):
    #     context = super(CategoryEditView, self).get_context_data()
    #     context['model_name'] = self.model._meta.model_name
    #     return context
    
    # def get_success_url(self):
    #     return reverse('category-list')