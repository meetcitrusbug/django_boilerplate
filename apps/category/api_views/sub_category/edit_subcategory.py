from rest_framework.generics import UpdateAPIView
from category.models import SubCategory
from rest_framework.status import HTTP_200_OK
from rest_framework.response import Response
from category.serializers import AddSubCategorySerializer


class EditSubCategoryAPIView(UpdateAPIView):
    
    serializer_class = AddSubCategorySerializer
    model = SubCategory
    queryset = model.objects.all()
    lookup_field = 'id'
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
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