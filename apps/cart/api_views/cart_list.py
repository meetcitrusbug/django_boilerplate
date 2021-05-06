from rest_framework.generics import ListAPIView
from cart.models import Cart
from cart.serializers import CartListSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class CartListAPIView(ListAPIView):
    
    model = Cart
    serializer_class = CartListSerializer
    permission_classes = [IsAuthenticated]
    
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        
        return Response({
            "status":True,
            "code":status.HTTP_200_OK,
            "message":"Category fetch successfully",
            "data":serializer.data
        }, status.HTTP_200_OK )
    
    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)