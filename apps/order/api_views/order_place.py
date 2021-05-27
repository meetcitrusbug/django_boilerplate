from django.db.models import Sum
from django.db.models import F

from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status

from order.serializers import OrderPlaceSerializer
from order.models import Order
from cart.models import Cart

class OrderPlaceAPIView(CreateAPIView):
    
    serializer_class = OrderPlaceSerializer
    model = Order
    queryset = model.objects.all()
        
    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        data['user'] = request.user.pk
        data['total_amount'] = self.get_total_price(request.user)
        data['products'] = self.get_products(request.user)
        
        if not data['total_amount']  or data['total_amount'] <= 0:
            return Response({
            "code":status.HTTP_200_OK,
            "status":False,
            "message":"can not processed with 0 amount",
            "data": {}
            }, status=status.HTTP_200_OK)
        
        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            
            return Response({
                "code":status.HTTP_200_OK,
                "status":True,
                "message":"Order placed successfully",
                "data": serializer.data
                }, status=status.HTTP_200_OK, headers=headers)
        else:
            return Response({
                "code":status.HTTP_200_OK,
                "status":False,
                "message":"Please fill missing fields or solve errors",
                "data": serializer.errors
                }, status=status.HTTP_200_OK)
            
    def get_total_price(self, user):
        total_price = Cart.objects.filter(user=user).values('user').aggregate(
                                    total_price=Sum(F('product__price')* F("quantity")))
        return total_price.get('total_price',0)

    def get_products(self, user):
        products = Cart.objects.filter(user=user).values('product','quantity')
        return list(products)