from rest_framework.generics import DestroyAPIView
from category.models import Category
from rest_framework.status import HTTP_200_OK
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class DeleteCategoryAPIView(DestroyAPIView):
    
    model = Category
    queryset = model.objects.all()
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]
    
    def delete(self, request, *args, **kwargs):
        
        instance = self.get_object()
        if instance:
            self.perform_destroy(instance)
            return Response({
                "status":True,
                "code":HTTP_200_OK,
                "message":"Category delete successfully",
                "data":{}
                }, HTTP_200_OK)
        
        return Response({
            "status":True,
            "code":HTTP_200_OK,
            "message":"Category not found",
            "data":{}
            }, HTTP_200_OK)