from django.views.generic import CreateView
from category.forms import AddSubCategoryForm
from category.models import SubCategory
from django.shortcuts import reverse
from django_boilerplate.views.generic import (
    MyNewFormsetCreateView,
)

class SubCategoryAddView(MyNewFormsetCreateView):
    
    model = SubCategory
    form_class = AddSubCategoryForm
    template_name = 'subcategory/subcategory_add.html'
    permission_required = ("add_subcategory",)
