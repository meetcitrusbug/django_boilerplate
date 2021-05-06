from rest_framework import serializers
from cart.models import Cart
from product.serializers import PorductDetailsSerializer

class CartListSerializer(serializers.ModelSerializer):
    
    product = PorductDetailsSerializer()
    
    class Meta:
        model = Cart
        fields = ('id', 'product', 'quantity')