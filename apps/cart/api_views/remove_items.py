from rest_framework import status
from rest_framework.generics  import DestroyAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from cart.models import Cart

class RemoveItemsAPIView(DestroyAPIView):
    
    model = Cart
    
    def delete(self, request, *args, **kwargs):
        
        queryset = self.get_queryset()
        
        if queryset:
            self.perform_destroy(queryset)
            return Response({
                "status":True,
                "code":status.HTTP_200_OK,
                "message":"Items deleted",
                "data":{}
            }, status.HTTP_200_OK )

        return Response({
            "status":False,
            "code":status.HTTP_200_OK,
            "message":"No items for delete",
            "data":{}
        }, status.HTTP_200_OK )
        
        
    def perform_destroy(self, queryset):
        queryset.delete()
        
    def get_queryset(self):
        items = self.request.data.get('items', [])
        return  self.model.objects.filter(id__in=items, user=self.request.user)