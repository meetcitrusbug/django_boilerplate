from rest_framework.generics import ListAPIView
from category.serializers import SubCategorySerializer
from category.models import SubCategory
from rest_framework.response import Response
from rest_framework import status

class SubCategoryListAPIView(ListAPIView):
    
    serializer_class = SubCategorySerializer
    queryset = SubCategory.objects.all()
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            "status":True,
            "code":status.HTTP_200_OK,
            "message":"Subcategory fetch successfully",
            "data":serializer.data
        }, status.HTTP_200_OK )
        
    def filter_queryset(self, queryset):
        category = self.request.query_params.get('category')
        search = self.request.query_params.get('search')
        sort = self.request.query_params.get('sort')
        if category:
            queryset = queryset.filter(category=category)
        if search:
            queryset = queryset.filter(name__icontains=search)
        if sort:
            queryset = queryset.order_by(sort)
        return queryset.filter(is_active=True)