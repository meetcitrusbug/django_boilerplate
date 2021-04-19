from rest_framework import serializers
from product.models import Product, ProductImage, ProductTag
from .product import ProductImageSerializer, ProductTagSerializer

class ProductCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = ['id', 'name', 'user', 'product_number', 'description',
                  'sub_category', 'product_shipping_method', 'status',
                  'price', 'is_refundable']

        
    def save(self, *args, **kwargs):
        
        instance = super(ProductCreateSerializer, self).save()
        
        request = self.context.get('request')
        images = request.data.getlist('image')
        tags = request.data.getlist('tag')
        
        product_image_data = []
        product_tags_data = []
        
        for image in images:
            product_image_data.append({
                            'image':image,
                            'product':instance.pk})

        for tag in tags:
            product_tags_data.append({
                            'tag':tag,
                            'product':instance.pk})
        
            
        ## save multiple images
        self.image_serializer = ProductImageSerializer(
                    data=product_image_data, many=True)
        self.image_serializer.is_valid()
        self.image_instances = self.image_serializer.save()
        
        ## save multiple tag
        self.tag_serializer = ProductTagSerializer(data=product_tags_data, many=True)
        self.tag_serializer.is_valid()
        self.tag_instances = self.tag_serializer.save()
        
        return instance
    
    def to_representation(self, instance):
        ret = super(ProductCreateSerializer, self).to_representation(instance)
        ret['images']= self.image_serializer.to_representation(self.image_instances)
        ret['tags']= self.tag_serializer.to_representation(self.tag_instances)
        return ret
        