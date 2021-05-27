from django.db.models import Q

from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response

from order.serializers import OrderListSerializer
from apps.utils.pagination import ProductPagination
from order.models import Order

class OrderListAPIView(ListAPIView):
    
    model = Order
    permission_classes = [IsAuthenticated]
    serializer_class = OrderListSerializer
    pagination_class = ProductPagination
    
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
            "message":"Order fetch successfully",
            "data":serializer.data
        }, status.HTTP_200_OK )
        
    def get_queryset(self):
        
        query = self.model.objects.filter(user=self.request.user)
        
        search = self.request.GET.get('search', '')
        date_lte = self.request.GET.get('date_lte', '')
        date_gte = self.request.GET.get('date_gte', '')

        if search:
            query = query.filter(Q(user__email=search) | Q(order_id=search) )
        if date_gte:
            query = query.filter(created_at__gte=date_gte)
        if date_lte:
            query = query.filter(created_at__lte=date_lte)
        
        return query.order_by('-id')