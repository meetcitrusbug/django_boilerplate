# -*- coding: utf-8 -*-
"""
To customize the API response.
"""

from rest_framework import status
from rest_framework.response import Response

from . utils import modify_api_response


def MyAPIResponse(data=None, code=status.HTTP_200_OK):
    """Custom API response format."""
    return modify_api_response(Response(data, status=code))
