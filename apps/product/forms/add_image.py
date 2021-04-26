from product.models import ProductImage
from django import forms 


class AddProductImageForm(forms.ModelForm):
    
    class Meta:
        model = ProductImage
        fields = ['id', 'image', 'product']
    