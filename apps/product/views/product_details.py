from product.models import Product
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView
from product.serializers import PorductDetailsSerializer


class PorductDetailsAPIView(RetrieveAPIView):
    
    serializer_class = PorductDetailsSerializer
    queryset = Product.objects.all()
    lookup_field = ['id']
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        message = 'Product fetch successfully'
        status_ =  True
        if not instance:
            message ='Product does\'t found'
            status_ = False
            
        serializer = self.get_serializer(instance, context={'request':request})
        return  Response({
                    "status":status_,
                    "code":status.HTTP_200_OK,
                    "message":message,
                    "data":serializer.data if status_ else {},
                    }, status.HTTP_200_OK )
        
    def get_object(self):
        id = self.kwargs.get('id')
        try:
            return Product.objects.get(id=id)
        except Product.DoesNotExist:
            return None