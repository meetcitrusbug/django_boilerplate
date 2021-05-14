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