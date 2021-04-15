from product.models import Product
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from product.serializers import ProductListSerializer


class ProductListViewAPI(ListAPIView):
    
    serializer_class = ProductListSerializer
    model = Product
    queryset = model.objects.all()
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True, context={'request':self.request})
        return Response({
            "status":True,
            "code":status.HTTP_200_OK,
            "message":"Products fetch successfully",
            "data":serializer.data
        }, status.HTTP_200_OK )
        
    def filter_queryset(self, queryset):
        queryset = queryset.filter(is_active=True)
        
        search = self.request.query_params.get('search')
        filter_ = self.request.query_params.get('filter')
        sort = self.request.query_params.get('sort')
        
        if search:
            queryset = queryset.filter(name__icontains=search)
        if filter_:
            queryset = queryset.filter(status=filter_)
        if sort:
            queryset = queryset.order_by(sort)
            
        return queryset