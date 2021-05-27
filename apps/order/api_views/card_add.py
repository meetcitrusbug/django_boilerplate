from django.conf import settings

from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

import stripe

from order.models import UserCard
from order.serializers import CardAddSerializer

class CardAddAPIView(CreateAPIView):
    
    model = UserCard
    permission_classes = [IsAuthenticated]
    stripe.api_key = settings.STRIPE_SECRET_KEY
    serializer_class = CardAddSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={'request':request})
        if serializer.is_valid():
            serializer.save()
            headers = self.get_success_headers(serializer.data)
            return Response(
                data={
                    'code':status.HTTP_200_OK,
                    'status':True,
                    'message':"Card added",
                    'data':serializer.data
                    },
                status=status.HTTP_200_OK,
                headers=headers)
        else:
            return Response(
                data={
                    'code':status.HTTP_200_OK,
                    'status':False,
                    'message':"Solved error or fill missing fields",
                    'data':serializer.errors
                    },
                status=status.HTTP_200_OK)