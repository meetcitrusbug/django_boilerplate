from django import forms
from product.models import ProductTag


class AddProductTagForm(forms.ModelForm):
    
    class Meta:
        model = ProductTag
        fields = ['id', 'tag', 'product']