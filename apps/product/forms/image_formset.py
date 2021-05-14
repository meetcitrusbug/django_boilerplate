from django.forms import modelformset_factory
from django import forms
from product.models import ProductImage
from extra_views import InlineFormSetFactory


class ProductImageForm(forms.ModelForm):
    
    class Meta:
        model = ProductImage
        fields = ['id', 'image', 'product']


class ProductImageFormset(InlineFormSetFactory):
    """Inline view to show Skill within the Parent View"""
    
    model = ProductImage
    form_class = ProductImageForm
    factory_kwargs = {'extra': 1, 'max_num': None, 'can_order': False, 'can_delete': True}