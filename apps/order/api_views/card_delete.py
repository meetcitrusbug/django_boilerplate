import stripe
from rest_framework.generics import DestroyAPIView
from order.models import UserCard
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.conf import settings

class CardDeleteAPIView(DestroyAPIView):
    
    model = UserCard
    permission_classes = [IsAuthenticated]
    stripe.api_key = settings.STRIPE_SECRET_KEY
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance:
            try:
                stripe.Customer.delete_source(
                        instance.user.customer_id,
                        instance.card_number,
                        )
                self.perform_destroy(instance)
                return Response({
                    "code":status.HTTP_200_OK,
                    "status":True,
                    "message":'Card deleted'
                    },
                    status=status.HTTP_200_OK)
            except Exception as e:
                return Response({
                        "code":status.HTTP_200_OK,
                        "status":False,
                        "message":'Card not found'
                    },
                    status=status.HTTP_200_OK)
                
        return Response({
                "code":status.HTTP_200_OK,
                "status":False,
                "message":'Card not found'
                },
                status=status.HTTP_200_OK)
            
    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)
    
    def perform_destroy(self, instance):
        instance.delete()