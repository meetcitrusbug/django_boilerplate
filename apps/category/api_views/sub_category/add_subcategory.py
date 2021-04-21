from rest_framework.generics import CreateAPIView
from category.models import SubCategory
from rest_framework.status import HTTP_200_OK
from rest_framework.response import Response
from category.serializers import AddSubCategorySerializer


class AddSubCategoryAPIView(CreateAPIView):
    
    serializer_class = AddSubCategorySerializer
    model = SubCategory
    queryset = model.objects.all()
    
    def create(self, request, *args, **kwargs):
        
        serializer = self.get_serializer(data=request.data)
        is_valid = serializer.is_valid()
        
        if is_valid:
            serializer.save()
            return Response({
                "status":True,
                "code":HTTP_200_OK,
                "message":"subcategory save successfully",
                "data":serializer.data,
                },HTTP_200_OK)
        
        return Response({
                "status":True,
                "code":HTTP_200_OK,
                "message":"subcategory save successfully",
                "data":serializer.errors,
                },HTTP_200_OK)