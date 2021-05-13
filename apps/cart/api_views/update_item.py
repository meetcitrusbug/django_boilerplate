from rest_framework.generics import UpdateAPIView
from cart.serializers import AddItemsSerializer
from rest_framework.permissions import IsAuthenticated
from cart.models import Cart
from django_boilerplate.utils.api import modify_api_response
from rest_framework.response import Response
from rest_framework import status

class UpdateItemsAPIView(UpdateAPIView):
    
    serializer_class = AddItemsSerializer
    permission_classes = [IsAuthenticated]
    model = Cart
    
    def update(self, request, *args, **kwargs):
        
        instance = self.get_objects(kwargs.get('pk'))
        if not instance:
            return Response({
                    "status":False,
                    "code":status.HTTP_200_OK,
                    "message":"Cart instance not found!",
                    "data":serializer.errors
                    }, status.HTTP_200_OK )
            
        serializer = self.get_serializer(data=request.data, instance=instance,
                                         many=False,partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status":True,
                "code":status.HTTP_200_OK,
                "message":"Items added in cart",
                "data":serializer.data
            }, status.HTTP_200_OK )
            
        return Response({
            "status":False,
            "code":status.HTTP_200_OK,
            "message":"Please fill missing field or solve error",
            "data":serializer.errors
        }, status.HTTP_200_OK )
            
    def get_serializer(self, *args, **kwargs):
        return self.serializer_class(*args, **kwargs)
    
    def get_objects(self, pk):
        try:
            return Cart.objects.get(pk=pk)
        except Cart.DoesNotExist:
            return None