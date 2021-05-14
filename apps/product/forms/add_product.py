from product.models import Product
from django import forms 


class AddProductForm(forms.ModelForm):
    
    product_number = forms.CharField(required=True)
    
    class Meta:
        model = Product
        fields = ['name', 'user', 'product_number', 'description', 'sub_category',
                  'product_shipping_method', 'status', 'price', 'is_refundable', 'is_active']
        widgets = {
                'price': forms.NumberInput(attrs={'min': '0'}),
            }