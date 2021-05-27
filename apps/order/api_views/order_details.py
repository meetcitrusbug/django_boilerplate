from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from order.models import Order
from order.serializers import OrderDetailsSerializer


class OrderDetailsAPIView(RetrieveAPIView):
    
    model = Order
    serializer_class = OrderDetailsSerializer
    permission_classes = (IsAuthenticated,)
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(
            {  
                "code":status.HTTP_200_OK,
                "status":True,
                "message":"Payment details fetch successfully",
                "data":serializer.data
            },status.HTTP_200_OK)
    
    def get_queryset(self):
        return self.model.objects.filter(
            user = self.request.user,
            pk = self.kwargs.get('pk')    
        )