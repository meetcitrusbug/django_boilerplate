from rest_framework import serializers
from product.models import Product, ProductImage
from .product import ProductImageSerializer

class ProductUpdateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = ['id','name', 'product_number', 'description',
                  'sub_category', 'product_shipping_method', 'status',
                  'price', 'is_refundable']

    def save(self, *args, **kwargs):
        
        instance = super(ProductUpdateSerializer, self).save()
        
        request = self.context.get('request')
        images = request.data.getlist('image')
        product_image_data = []
        
        for image in images:
            product_image_data.append({
                            'image':image,
                            'product':instance.pk})
            
        self.image_serializer = ProductImageSerializer(
                    data=product_image_data, many=True)
        self.image_serializer.is_valid()
        self.instances = self.image_serializer.save()
        
        return instance
    
    def to_representation(self, instance):
        ret = super(ProductUpdateSerializer, self).to_representation(instance)
        ret['images']= self.image_serializer.to_representation(self.instances)
        return ret