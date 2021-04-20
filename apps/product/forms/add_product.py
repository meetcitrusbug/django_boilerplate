from product.models import Product
from django import forms 


class AddProductForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = ['name', 'user', 'product_number', 'description', 'sub_category',
                  'product_shipping_method', 'status', 'price', 'is_refundable', 'is_active']
    
    # def save(self):
    #     print(self.cleaned_data)
    #     instance = super(AddProductForm, self).save()
    #     return instance
         