from django.conf import settings

from rest_framework import serializers
from rest_framework.exceptions import APIException

import stripe

from order.models import Order, UserCard

class CardAddSerializer(serializers.Serializer):
    
    transaction_id = serializers.CharField()
    stripe.api_key = settings.STRIPE_SECRET_KEY
    
    def save(self):
        data = self.validated_data
        request = self.context.get('request')
        user =  request.user
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
            raise APIException(e)