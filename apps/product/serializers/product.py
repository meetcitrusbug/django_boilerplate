from rest_framework import serializers
from product.models import Product, ProductImage

class ProductListSerializer(serializers.ModelSerializer):
    
    image = serializers.SerializerMethodField('get_image')
    
    class Meta:
        model = Product
        fields = ['id', 'name',  'image', 'status', 'sub_category', 'price', 'is_refundable']
        
    def get_image(self, obj):
        image_obj = ProductImage.objects.select_related('product').filter(product=obj).first()
        request = self.context.get('request')
        if image_obj:
            return  request.build_absolute_uri(image_obj.image.url)
        return ''

    
class ProductImageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProductImage
        fields = ['id', 'image']


