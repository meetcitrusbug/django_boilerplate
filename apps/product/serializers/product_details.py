from rest_framework import serializers
from .product import ProductImageSerializer
from product.models import Product, ProductImage

class PorductDetailsSerializer(serializers.ModelSerializer):
    
    images = serializers.SerializerMethodField('get_images')
    
    class Meta:
        model = Product
        fields = ['id', 'name', 'product_number', 'description', 'status', 'sub_category', 'price', 
                  'product_shipping_method', 'is_refundable', 'images']
        
    def get_images(self, obj):
        images = ProductImage.objects.select_related('product').filter(product=obj)
        request = self.context.get('request')
        return ProductImageSerializer(images, many=True, context={'request':request}).data