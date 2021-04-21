from rest_framework.generics import CreateAPIView
from category.serializers import AddCategorySerializer
from category.models import Category
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

class AddCategoryAPIView(CreateAPIView):
    
    serializer_class = AddCategorySerializer
    model = Category
    permission_classes = [IsAuthenticated]
    
    
    def create(self, request, *args, **kwargs):
        
        serializer = self.get_serializer(data=request.data)
        is_valid = serializer.is_valid()
        
        if is_valid:
            serializer.save()
            return Response({
                "status":True,
                "code":HTTP_200_OK,
                "message":"Category save successfully",
                "data":serializer.data
                } ,HTTP_200_OK)
            
        return Response({
            "status":False,
            "code":HTTP_200_OK,
            "message":"Please fill missing fields or sovle error!",
            "data":serializer.errors
            } ,HTTP_200_OK)