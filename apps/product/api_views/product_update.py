from product.models import Product
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import UpdateAPIView
from product.serializers import ProductUpdateSerializer
from rest_framework.permissions import IsAuthenticated



class ProductUpdateAPIView(UpdateAPIView):
    
    queryset = Product.objects.all()
    serializer_class = ProductUpdateSerializer
    lookup_field = 'id'


    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        is_valid = serializer.is_valid()
        
        if not is_valid: 
            return  Response({"status":False,
                            "code":status.HTTP_200_OK,
                            "message":"Please fill missing field or solve error",
                            "data":{},
                            }, status.HTTP_200_OK )
            
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return  Response({ "status":True,
                        "code":status.HTTP_200_OK,
                        "message":"Product updated successfully",
                        "data":serializer.data,
                        }, status.HTTP_200_OK )