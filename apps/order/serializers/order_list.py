from rest_framework import serializers
from order.models import Order, OrderProduct
from .card_list import CardListSerializer
from .address import AddressSerializer


class OrderProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = OrderProduct
        fields = '__all__'

class OrderListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Order
        fields = ('id', 'order_id', 'user', 'card', 'total_amount', 'status', 'billing_address', 'shipping_address',
                  'created_at')