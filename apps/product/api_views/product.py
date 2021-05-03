from product.models import Product, ProductTag
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from product.serializers import ProductListSerializer
from apps.utils.pagination import ProductPagination
from django.db.models import Q

class ProductListViewAPI(ListAPIView):
    
    serializer_class = ProductListSerializer
    pagination_class = ProductPagination
    model = Product
    queryset = model.objects.all()
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        
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
        category = self.request.query_params.get('category')
        sub_category = self.request.query_params.get('sub_category')
        price = self.request.query_params.get('price')
        price_gt = self.request.query_params.get('price_gt')
        price_lt = self.request.query_params.get('price_lt')

        if search:
            product_id = ProductTag.objects.filter(tag__icontains=search).values_list('product', flat=True)
            queryset = queryset.filter(Q(id__in=product_id) | Q(name__icontains=search) | Q(product_number__icontains=search))
        if filter_:
            queryset = queryset.filter(status=filter_)
        if sort:
            queryset = queryset.order_by(sort)
        if category:
            category = category.split(',')
            queryset = queryset.filter(sub_category__category__in=category)
        if sub_category:
            sub_category = sub_category.split(',')
            queryset = queryset.filter(sub_category__in=sub_category)
        if price:
            queryset = queryset.filter(price=price)
        if price_gt:
            queryset = queryset.filter(price__gte=price_gt)
        if price_lt:
            queryset = queryset.filter(price__lte=price_lt)
            
        return queryset