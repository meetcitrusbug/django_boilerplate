from django.views import View
from django.conf import settings
from django.shortcuts import redirect

import stripe

from order.models import Order, UserCard


class CardDefaultView(View):
    
    def get(self, request, pk):
        instance = self.get_object(pk)
        try:
            stripe.Customer.modify(
                instance.user.customer_id,
                default_source=instance.card_number,
                )
            instance.is_default=True
            instance.save()
            self.update_other_card(instance)
        except Exception as e:
            print('==============',e)
        
        return redirect('cards')
    
    def update_other_card(self, instance):
        UserCard.objects.filter(user=instance.user).exclude(
                                        pk=instance.pk).update(
                                                        is_default=False)

    def get_object(self, pk):
        try:
            return UserCard.objects.get(pk=pk)
        except UserCard.DoesNotExist:
            return None