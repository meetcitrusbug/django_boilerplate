from django.conf import settings

from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

import stripe

from order.models import UserCard
from order.serializers import CardDafaultSerializer

class CardDefaultView(UpdateAPIView):
    
    model = UserCard
    permission_classes = [IsAuthenticated]
    serializer_class = CardDafaultSerializer
    
    def update(self, request, *args, **kwargs):
        self.request = request      
        instance = self.get_object(kwargs.get('pk'))
        
        if not instance:
            return Response(
                data={
                    'code':status.HTTP_200_OK,
                    'status':False,
                    'message':"Card not found",
                    'data':{}
                    },
                status=status.HTTP_200_OK)
        
        serializer = self.get_serializer(data=request.data, context={'request':request}, instance=instance)
        if serializer.is_valid():
            serializer.save()
            return Response(
                data={
                    'code':status.HTTP_200_OK,
                    'status':True,
                    'message':"Card upated",
                    'data':serializer.data
                    },
                status=status.HTTP_200_OK)
        else:
            return Response(
                data={
                    'code':status.HTTP_200_OK,
                    'status':False,
                    'message':"Solved error or fill missing fields",
                    'data':serializer.errors
                    },
                status=status.HTTP_200_OK)
    
    def get_object(self, pk):
        try:
            return UserCard.objects.get(pk=pk,user = self.request.user)
        except UserCard.DoesNotExist:
            return None