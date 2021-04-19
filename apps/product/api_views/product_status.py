from rest_framework.views import APIView
from product.models import Product
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.permissions import IsAuthenticated


class ProductStatusAPIView(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def post(self, request, pk, status):
        product = self.get_objects(pk)
        if not product:
            return Response(
                {
                    'code':HTTP_200_OK,
                    'status':False,
                    'message':"Product does't exits",
                    'data':{}
                }
                ,HTTP_200_OK)
        if status == 'inactive':
            product.is_active =  False
            product.save()
            return Response(
                {
                    'code':HTTP_200_OK,
                    'status':True,
                    'message':"Product inactivated!",
                    'data':{}
                }
                ,HTTP_200_OK)
        elif status == 'active':
            product.is_active =  True
            product.save()
            return Response(
                {
                    'code':HTTP_200_OK,
                    'status':True,
                    'message':"Product activated!",
                    'data':{}
                }
                ,HTTP_200_OK)
        else:
            return Response(
                {
                    'code':HTTP_200_OK,
                    'status':False,
                    'message':"Product status can't change",
                    'data':{}
                }
                ,HTTP_200_OK)
            
            
    
    def get_objects(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return None