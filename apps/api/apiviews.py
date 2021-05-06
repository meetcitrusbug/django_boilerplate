from rest_framework.views import APIView
from . utils import modify_api_response

class MyAPIView(APIView):

    def finalize_response(self, request, response, *args, **kwargs):
        response = modify_api_response(response)
        return super().finalize_response(request, response, *args, **kwargs)