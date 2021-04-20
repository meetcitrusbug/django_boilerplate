from django import forms
from category.models import SubCategory

class AddSubCategoryForm(forms.ModelForm):
    
    class Meta:
        model = SubCategory
        fields = ['id', 'name', 'category']