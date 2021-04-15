from product.models import ProductImage
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAuthenticated



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
