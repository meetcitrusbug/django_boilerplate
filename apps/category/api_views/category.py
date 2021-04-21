from rest_framework.generics import ListAPIView
from category.serializers import CategorySerializer
from category.models import Category
from rest_framework.response import Response
from rest_framework import status

class CategoryListAPIView(ListAPIView):
    
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    
    def list(self, requuest, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            "status":True,
            "code":status.HTTP_200_OK,
            "message":"Category fetch successfully",
            "data":serializer.data
        }, status.HTTP_200_OK )
        
    
    def filter_queryset(self, queryset):
        search = self.request.query_params.get('search')
        sort = self.request.query_params.get('sort')
        
        if search:
            queryset = queryset.filter(name__icontains=search)
        if sort:
            queryset = queryset.order_by(sort)
        return queryset.filter(is_active=True)