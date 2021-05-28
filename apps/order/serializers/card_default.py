from django.conf import settings

from rest_framework import serializers
from rest_framework.exceptions import APIException

import stripe

from order.models import Order, UserCard

class CardDafaultSerializer(serializers.Serializer):
    
    stripe.api_key = settings.STRIPE_SECRET_KEY
    
    def save(self):
        self.instance
        try:
            stripe.Customer.modify(
                self.instance.user.customer_id,
                default_source=self.instance.card_number,
                )
            self.instance.is_default=True
            self.instance.save()
            self.update_other_card()
            return self.instance
        except Exception as e:
            raise APIException(e)
    
    def update_other_card(self):
        UserCard.objects.filter(user=self.instance.user).exclude(
                                        pk=self.instance.pk).update(
                                                        is_default=False)