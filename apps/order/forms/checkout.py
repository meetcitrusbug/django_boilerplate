from django import forms
from django.conf import settings
from django.forms import ValidationError

import stripe

from order.models import Order, OrderProduct, Address, UserCard
from cart.models import Cart
from django_boilerplate.models import User
from order.serializers.order_place import OrderProductSerializer
from product.models import Product


class AddressForm(forms.ModelForm):
    
    class Meta:
        model = Address
        fields = ('id', 'street', 'city', 'state', 'country')

class CheckoutForm(forms.Form):
    
    stripe.api_key = settings.STRIPE_SECRET_KEY
    
    
    number = forms.CharField()
    name = forms.CharField(label='Cardholder name')
    cvc = forms.CharField()
    date = forms.DateField(label='Expiry date')
    save_card = forms.BooleanField(label='Want to save card?', required=False)
    user = forms.IntegerField(required=False)
    total_amount = forms.DecimalField(required=False)
    billing_address = AddressForm()
    shipping_address = AddressForm()
    

    def save(self, *args, **kwargs):
        validated_data= self.cleaned_data.copy()
        
        user = User.objects.filter(pk=validated_data['user']).first()
        user = self.create_stripe_user(user)
        validated_data['user'] = user
        products = self.get_products(user)
        is_save_card = validated_data.pop('save_card', False)

        #Save order
        instance = Order()
        instance.transaction_id = self.generate_token(validated_data)
        instance.user = validated_data['user']
        instance.total_amount = validated_data['total_amount']

        
            
        if is_save_card:
            instance = self.process_payment_with_saving_card(instance)
        else:
            instance = self.process_payment_with_token(instance)

        instance.save()
        
        #Save order product list
        for product in products:
            product['order'] = instance
            product['amount'] = product['product'].price
            OrderProduct.objects.create(**product)
        
          
        
        self.clear_cart(instance.user)
        
        return instance
    
    def generate_token(self, data):
        try:
            stripe_token = stripe.Token.create(
                    card={
                            "number": data.get('number'),
                            "exp_month": data.get('date').strftime("%m"),
                            "exp_year": data.get('date').strftime("%Y"),
                            "cvc": data.get('cvc'),
                            "name": data.get('name')
                        }
                )
            return  stripe_token['id']
        except Exception as e:
            raise ValidationError(e)
    
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
            raise ValidationError(e)
        
        return instance
    
    
    def get_products(self, user):
        products = Cart.objects.filter(user=user).values('product','quantity')
        for product in products:
            product['product'] = Product.objects.filter(pk=product['product']).first()
        return list(products)
    
        
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
            raise ValidationError(e)
        

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
                raise ValidationError(e)
        else:
            return user
        


    def clear_cart(self, user):
        Cart.objects.filter(user=user).delete()
        
        
        
        
class CheckoutCardForm(forms.ModelForm):
    
    stripe.api_key = settings.STRIPE_SECRET_KEY
    

    total_amount = forms.DecimalField(required=False)   


    class Meta:
        model = Order
        fields = ('user', 'total_amount', 'card')


    def save(self, *args, **kwargs):
        validated_data= self.cleaned_data.copy()
                
        products = self.get_products(validated_data['user'])
               
        #Save order
        instance = Order()
        instance.card = validated_data['card']
        instance.user = validated_data['user']
        instance.total_amount = validated_data['total_amount']
                 
        instance = self.process_payment_with_card(instance)
        
        #Save billing_address and shipping_address
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
            raise ValidationError(e)
        
        return instance
    
    def clear_cart(self, user):
        Cart.objects.filter(user=user).delete()
        
    
    
    def get_usercard(self, pk):
        try:
            return UserCard.objects.get(pk=pk)
        except Exception as e:
            raise ValidationError(e)
        
    def get_products(self, user):
        products = Cart.objects.filter(user=user).values('product','quantity')
        for product in products:
            product['product'] = Product.objects.filter(pk=product['product']).first()
        return list(products)