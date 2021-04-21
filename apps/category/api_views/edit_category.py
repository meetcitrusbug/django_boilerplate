from rest_framework.generics import UpdateAPIView
from category.serializers import AddCategorySerializer
from category.models import Category
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

class EditCategoryAPIView(UpdateAPIView):
    
    serializer_class = AddCategorySerializer
    model = Category
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'
    
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance,data=request.data, partial=partial)
        is_valid = serializer.is_valid()
        
        if not is_valid: 
            return  Response({"status":False,
                            "code":HTTP_200_OK,
                            "message":"Please fill missing field or solve error",
                            "data":serializer.errors,
                            }, HTTP_200_OK )
            
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return  Response({ "status":True,
                        "code":HTTP_200_OK,
                        "message":"Category updated successfully",
                        "data":serializer.data,
                        }, HTTP_200_OK )
    
    def get_queryset(self):
        
        return self.model.objects.all()