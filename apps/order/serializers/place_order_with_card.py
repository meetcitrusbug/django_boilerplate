from rest_framework import serializers
from order.models import Order, OrderProduct, Address, UserCard
from cart.models import Cart
import stripe
from django.conf import settings
from rest_framework.exceptions import APIException

class OrderProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = OrderProduct
        fields = ('product', 'quantity')


class AddressSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Address
        fields = '__all__'

        
class PlaceOrderWithCardSerializer(serializers.ModelSerializer):
    
    products = OrderProductSerializer('product_set', many=True)
    billing_address = AddressSerializer('billing_address_set', write_only=True)
    shipping_address = AddressSerializer('shipping_address_set', write_only=True)
    card = serializers.PrimaryKeyRelatedField(read_only=False, queryset=UserCard.objects.all())
    
    stripe.api_key = settings.STRIPE_SECRET_KEY
    
    class Meta:
        model = Order
        fields = ('user', 'total_amount', 'card', 'billing_address', 'shipping_address', 'products')
        
    def save(self, *args, **kwargs):
        validated_data= self.validated_data.copy()
                
        products = validated_data.pop('products', [])
        is_save_card = validated_data.pop('is_save_card', False)
        
        
               
        #Save order
        instance = Order()
        instance.card = validated_data['card']
        instance.user = validated_data['user']
        instance.total_amount = validated_data['total_amount']
                 
        instance = self.process_payment_with_card(instance)
        
        #Save billing_address and shipping_address        
        instance.billing_address = Address.objects.create(**validated_data['billing_address'])
        instance.shipping_address = Address.objects.create(**validated_data['shipping_address'])
        instance.save()
        
        #Save order product list
        for product in products:
            product['order'] = instance
            product['amount'] = product['product'].price
            OrderProduct.objects.create(**product)
            
        self.clear_cart(instance.user)
        
        return instance
    
    
    def process_payment_with_card(self, instance):
        """
            Saving card with all details 
        """
        try:
            actual_price = instance.total_amount*100
            
            stripe_transaction = stripe.Charge.create(
                amount=actual_price,
                currency=settings.CURRENCY,
                customer=instance.user.customer_id,
                source=instance.card.card_number,
                description="Order",
            )
            
            instance.transaction_id = stripe_transaction['id']
            return instance
        except Exception as e:
            raise APIException(e)
        
        return instance
    
    def clear_cart(self, user):
        Cart.objects.filter(user=user).delete()