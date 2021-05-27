from django import forms
from django.conf import settings
from django.forms import ValidationError

import stripe

from order.models import Order, OrderProduct, Address, UserCard
from cart.models import Cart
from django_boilerplate.models import User

class CardAddForm(forms.Form):
    
    stripe.api_key = settings.STRIPE_SECRET_KEY
    
    
    number = forms.CharField()
    name = forms.CharField(label='Cardholder name')
    cvc = forms.CharField()
    date = forms.DateField(label='Expiry date')
    
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request", {})
        super().__init__(*args, **kwargs)    
    

    def save(self):
        data = self.cleaned_data
        data['transaction_id'] = self.generate_token(data)
    
        user =  self.request.user
        try:
            card = stripe.Customer.create_source(
                user.customer_id,
                source=data['transaction_id'],
            )

            card['card_number']= card['id']
            card['id'] = None
            card['user'] = user
            
            return UserCard.objects.create(
                **card
            )
        except Exception as e:
            raise ValidationError(e)
    
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
    
