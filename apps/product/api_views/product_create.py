from product.models import Product
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from product.serializers import ProductCreateSerializer


class PrductCreateAPIView(CreateAPIView):
    
    permission_classes = [IsAuthenticated]
    serializer_class = ProductCreateSerializer
    
    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        data['user'] = request.user.pk
        serializer = self.get_serializer(data=data, context={'request':request})
        is_valid = serializer.is_valid()
        
        if not is_valid:
            return  Response({
                "status":False,
                "code":status.HTTP_200_OK,
                "message":"Please fill missing field or solve error",
                "data":serializer.errors,
                }, status.HTTP_200_OK )
                    
        self.perform_create(serializer)

        return  Response({
                    "status":True,
                    "code":status.HTTP_200_OK,
                    "message":"Product created successfully",
                    "data":serializer.data,
                    }, status.HTTP_200_OK )
