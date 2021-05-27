from rest_framework import serializers
from order.models import Order, OrderProduct, Address, UserCard
import stripe
from django.conf import settings
from rest_framework.exceptions import APIException
from cart.models import Cart

class OrderProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = OrderProduct
        fields = ('product', 'quantity')


class AddressSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Address
        fields = '__all__'

        
class OrderPlaceSerializer(serializers.ModelSerializer):
    
    products = OrderProductSerializer('product_set', many=True)
    billing_address = AddressSerializer('billing_address_set', write_only=True)
    shipping_address = AddressSerializer('shipping_address_set', write_only=True)
    is_save_card = serializers.BooleanField()
    
    stripe.api_key = settings.STRIPE_SECRET_KEY
    
    class Meta:
        model = Order
        fields = ('transaction_id', 'user', 'total_amount', 'billing_address', 'shipping_address', 'products', 'is_save_card')
        
    def save(self, *args, **kwargs):
        validated_data= self.validated_data.copy()
        
        user = validated_data['user']
        user = self.create_stripe_user(user)
        validated_data['user'] = user
        
        products = validated_data.pop('products', [])
        is_save_card = validated_data.pop('is_save_card', False)
        
        #Save billing_address and shipping_address
        
        #Save order
        instance = Order()
        instance.transaction_id = validated_data['transaction_id']
        instance.user = validated_data['user']
        instance.total_amount = validated_data['total_amount']
            
        if is_save_card:
            instance = self.process_payment_with_saving_card(instance)
        else:
            instance = self.process_payment_with_token(instance)
            
        
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
    
    
    def process_payment_with_saving_card(self, instance):
        """
            Saving card with all details 
        """
        try:
            card = stripe.Customer.create_source(
                instance.user.customer_id,
                source=instance.transaction_id,
            )
            card['card_number']= card['id']
            card['id'] = None
            card['user'] = instance.user
            instance.card = UserCard.objects.create(
                **card
            )
            
            actual_price = int(instance.total_amount)*100
            
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
    
        
    def process_payment_with_token(self, instance):
        """
            process payment with token
        """
        try:
            actual_price = int(instance.total_amount)*100
            stripe_transaction = stripe.Charge.create(
                amount=actual_price,
                currency=settings.CURRENCY,
                source=instance.transaction_id,
                description="Order",
            )
            instance.transaction_id = stripe_transaction['id']
            return instance
        except Exception as e:
            raise APIException(e)
        

    def create_stripe_user(self, user):
        """
        Create stripe customer if customer_id does not exists
        """
        if not user.customer_id:
            try:
                stripe_user =  stripe.Customer.create(
                            email=user.email
                        )
                user.customer_id = stripe_user['id']
                user.save()
                return user
            except Exception as e:
                raise APIException(e)
        else:
            return user
        
    def clear_cart(self, user):
        Cart.objects.filter(user=user).delete()
        
        

class OrderStatusUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ['status']