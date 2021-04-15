from rest_framework.pagination import PageNumberPagination
from rest_framework import status
from collections import OrderedDict
from rest_framework.response import Response

class ProductPagination(PageNumberPagination):
    page_size = 10

    def get_paginated_response(self, data):
    
        current = self.page.number
        next_page = 0 if self.get_next_link() is None else current + 1
        previous_page = 0 if self.get_previous_link() is None else current - 1
        
        return Response({
            "status":True,
            "code":status.HTTP_200_OK,
            "message":"Products fetch successfully",
            "data":OrderedDict([
                    ('links', {
                        'count':self.page.paginator.count,
                        'next': next_page,
                        'previous': previous_page,
                    }),
                    ('results', data)
        ])
        }, status.HTTP_200_OK)
        