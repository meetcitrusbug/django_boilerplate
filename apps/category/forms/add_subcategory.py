from django import forms
from category.models import SubCategory, Category
from extra_views import InlineFormSetFactory

class AddSubCategoryForm(forms.ModelForm):
    
    class Meta:
        model = SubCategory
        fields = ['id', 'name', 'category', 'image']
        
class SubCategoryFormset(InlineFormSetFactory):
    """Inline view to show Skill within the Parent View"""
    
    model = SubCategory
    form_class = AddSubCategoryForm
    factory_kwargs = {'extra': 1, 'max_num': None, 'can_order': False, 'can_delete': True}