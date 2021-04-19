from rest_framework import serializers
from product.models import Product, ProductImage, ProductTag
from .product import ProductImageSerializer, ProductTagSerializer

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
        
        ##save multiple images
        self.image_serializer = ProductImageSerializer(
                    data=product_image_data, many=True)
        self.image_serializer.is_valid()
        self.instances = self.image_serializer.save()
        
        
        self.delete_tags(self.instance)
        
        ##save multiple tag
        self.tag_serializer = ProductTagSerializer(data=product_tags_data, many=True)
        self.tag_serializer.is_valid()
        self.tag_instances = self.tag_serializer.save()
        
        
        return instance
    
    def to_representation(self, instance):
        ret = super(ProductUpdateSerializer, self).to_representation(instance)
        ret['images']= self.image_serializer.to_representation(self.instances)
        ret['tags']= self.tag_serializer.to_representation(self.tag_instances)
        return ret

    def delete_tags(self, product):
        ProductTag.objects.filter(product=product).delete()