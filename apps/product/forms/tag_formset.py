from django.forms.models import inlineformset_factory
from django import forms
from product.models import Product, ProductTag
from extra_views import InlineFormSetFactory

class ProductTagForm(forms.ModelForm):
    
    class Meta:
        model = ProductTag
        fields = ['id', 'tag', 'product']

class ProductTagFormset(InlineFormSetFactory):
    """Inline view to show Skill within the Parent View"""

    model = ProductTag
    form_class = ProductTagForm
    factory_kwargs = {'extra': 1, 'max_num': None, 'can_order': False, 'can_delete': True}