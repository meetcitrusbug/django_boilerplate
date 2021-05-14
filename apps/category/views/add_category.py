from django.views.generic import CreateView
from category.forms import AddCategoryForm, SubCategoryFormset
from category.models import Category, SubCategory
from django.shortcuts import reverse
from django_boilerplate.views.generic import (
    MyNewFormsetCreateView,
)

class CategoryAddView(MyNewFormsetCreateView):
    
    model = Category
    inline_model = SubCategory
    inlines = [SubCategoryFormset]
    form_class = AddCategoryForm
    template_name = 'category_add.html'
    permission_required = ("add_category",)
    