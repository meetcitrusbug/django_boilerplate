from rest_framework.generics import ListCreateAPIView
from cart.serializers import AddItemsSerializer
from rest_framework.permissions import IsAuthenticated
from cart.models import Cart
from django_boilerplate.utils.api import modify_api_response
from rest_framework.response import Response
from rest_framework import status

class AddItemsAPIView(ListCreateAPIView):
    
    serializer_class = AddItemsSerializer
    permission_classes = [IsAuthenticated]
    model = Cart
    
    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        
        for i in  data:
            i['user'] = request.user.pk
            
        serializer = self.get_serializer(data=request.data, *args, **kwargs, many=True)
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