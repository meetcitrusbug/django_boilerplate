from product.models import Product
from django import forms 
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

def validate_even(value):
    
    if not value:
        raise ValidationError(
            _('Price can not be empty'),
            params={'value': value},
        )
    elif value < 0:
        raise ValidationError(
            _('%(value)s can not be in minus'),
            params={'value': value},
        )
        
class AddProductForm(forms.ModelForm):
    
    product_number = forms.CharField(required=True)
    price = forms.IntegerField(validators=[validate_even])

    class Meta:
        model = Product
        fields = ['name', 'user', 'product_number', 'description', 'sub_category',
                  'product_shipping_method', 'status', 'price', 'is_refundable']
        widgets = {
                'price': forms.NumberInput(attrs={'min': '0'}),
            }