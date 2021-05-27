
from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from order.serializers import OrderStatusUpdateSerializer
from order.models import Order


class OrderStatusUpdateAPIView(UpdateAPIView):
    
    model = Order
    permission_classes = [IsAuthenticated]
    serializer_class = OrderStatusUpdateSerializer
    lookup_field = 'pk'
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            
            serializer.save()
            
            return Response({
                "code":status.HTTP_200_OK,
                "status":True,
                "data":serializer.data,
                "message":"Status updated"
                },status.HTTP_200_OK,)
        
        else:
            return Response({
                "code":status.HTTP_200_OK,
                "status":False,
                "data":serializer.errors,
                "message":"Please fill missing fields or solve error"
                },status.HTTP_200_OK,)
        

    
    def get_queryset(self):
        return self.model.objects.filter(
            user = self.request.user,
            pk=self.kwargs.get("pk")
        )