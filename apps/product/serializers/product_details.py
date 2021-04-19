from rest_framework import serializers
from .product import ProductImageSerializer, ProductTagSerializer
from product.models import Product, ProductImage, ProductTag

class PorductDetailsSerializer(serializers.ModelSerializer):
    
    images = serializers.SerializerMethodField('get_images')
    tags = serializers.SerializerMethodField('get_tags')
    
    class Meta:
        model = Product
        fields = ['id', 'name', 'product_number', 'description', 'status', 'sub_category', 'price', 
                  'product_shipping_method', 'is_refundable', 'images', 'tags']
        
    def get_images(self, obj):
        images = ProductImage.objects.select_related('product').filter(product=obj)
        request = self.context.get('request')
        return ProductImageSerializer(images, many=True, context={'request':request}).data
    
    def get_tags(self, obj):
        product_image = ProductTag.objects.filter(product=obj)
        return ProductTagSerializer(product_image, many=True).data