from rest_framework import serializers
from order.models import Order, OrderProduct
from .card_list import CardListSerializer
from .address import AddressSerializer
from product.serializers import PorductDetailsSerializer

class OrderProductSerializer(serializers.ModelSerializer):
    
    product = PorductDetailsSerializer()
    
    class Meta:
        model = OrderProduct
        fields = '__all__'

class OrderDetailsSerializer(serializers.ModelSerializer):
    
    card = CardListSerializer()
    billing_address = AddressSerializer()
    shipping_address = AddressSerializer()
    items = serializers.SerializerMethodField('get_items')
    
    class Meta:
        model = Order
        fields = ('id', 'order_id', 'user', 'card', 'total_amount', 'status', 'billing_address', 'shipping_address',
                  'created_at', 'items')
    
    def get_items(self, instance):
        queryset = OrderProduct.objects.filter(order=instance)
        return OrderProductSerializer(queryset, many=True).data