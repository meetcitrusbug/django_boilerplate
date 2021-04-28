from django.views.generic import UpdateView
from category.forms import AddSubCategoryForm
from category.models import SubCategory
from django.shortcuts import reverse
from django_boilerplate.views.generic import (
    MyNewFormsetUpdateView,
)

class SubCategoryEditView(MyNewFormsetUpdateView):
    
    model = SubCategory
    form_class = AddSubCategoryForm
    template_name = 'subcategory/subcategory_edit.html'
    permission_required = ("edit_subcategory",)