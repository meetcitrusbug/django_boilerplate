from django.forms.models import inlineformset_factory
from django import forms
from product.models import Product, ProductTag



class ProductTagForm(forms.ModelForm):
    
    class Meta:
        model = ProductTag
        fields = ['id', 'tag', 'product']


ProductTagFormset = inlineformset_factory(
    Product, ProductTag, form=ProductTagForm,
    fields=['tag'], extra=1, can_delete=True
)
    