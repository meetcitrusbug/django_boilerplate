
from django.conf import settings

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

import stripe

class GenerateStripeCartToken(APIView):
    
    permission_classes = [AllowAny]
    
    def post(self, request):
    
        stripe.api_key = settings.STRIPE_SECRET_KEY
        try:
            stripe_token = stripe.Token.create(
                card=request.data,
            )
            return Response({
                "code":status.HTTP_200_OK,
                "status":True,
                "message":"Token generated successfully",
                "data":stripe_token
            }, status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "code":status.HTTP_200_OK,
                "status":False,
                "message":str(e),
                "data":{}
            }, status.HTTP_200_OK)