from product.models import Product
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAuthenticated



class ProductDeleteAPIView(DestroyAPIView):
    
    queryset = Product.objects.all()
    lookup_field = 'id'
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({
            "status":True,
            "code":status.HTTP_200_OK,
            "message":"Products deleted successfully",
            "data":{}
        }, status.HTTP_200_OK )
