from django.forms import modelformset_factory
from django import forms
from product.models import ProductImage


ProductImageFormset = modelformset_factory(
    ProductImage,
    fields = (
        'image',
    ),
    extra=1,
    widgets = {
        'name':forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter image'
        })
    }
)