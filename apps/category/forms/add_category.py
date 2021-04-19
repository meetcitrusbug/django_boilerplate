from django import forms
from category.models import Category

class AddCategoryForm(forms.ModelForm):
    
    class Meta:
        model = Category
        fields = ['id', 'name']