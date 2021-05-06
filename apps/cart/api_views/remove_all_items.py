from rest_framework.generics  import DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from cart.models import Cart

class RemoveAllItemsAPIView(DestroyAPIView):
    
    model = Cart
    permission_classes = [IsAuthenticated]
    
    def destroy(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if queryset:
            self.perform_destroy(queryset)
            return Response({
                "status":True,
                "code":status.HTTP_200_OK,
                "message":"All items deleted",
                "data":{}
            }, status.HTTP_200_OK)
            
        return Response({
            "status":False,
            "code":status.HTTP_200_OK,
            "message":"No items for delete",
            "data":{}
        }, status.HTTP_200_OK)
    
    def perform_destroy(self, queryset):
        queryset.delete()
    
    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)