from product.models import ProductImage
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from product.serializers.product import ProductImageSerializer


class ProductImageAddAPIView(CreateAPIView):
    
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
    
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
        headers = self.get_success_headers(serializer.data)
        return  Response({
                    "status":True,
                    "code":status.HTTP_200_OK,
                    "message":"Product image added successfully",
                    "data":serializer.data,
                    }, status.HTTP_200_OK )



class ProductImageDeleteAPIView(DestroyAPIView):
    
    queryset = ProductImage.objects.all()
    lookup_field = 'id'
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({
            "status":True,
            "code":status.HTTP_200_OK,
            "message":"Image deleted successfully",
            "data":{}
        }, status.HTTP_200_OK )
