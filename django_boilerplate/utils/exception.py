"""
Define your custom exception function here.
"""

from rest_framework import status
from rest_framework.exceptions import APIException


class CustomValidation(APIException):
    """This is a custom validation exception to get the error details"""
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = 'A server error occurred.'

    def __init__(self, detail, status_code):
        """This method works as a constructor"""
        if status_code is not None:
            self.status_code = status_code
        # if detail is not None:
        #     self.detail = {field: force_text(detail)}
        #
        # else: self.detail = {'detail': force_text(self.default_detail)}
        self.detail = detail
