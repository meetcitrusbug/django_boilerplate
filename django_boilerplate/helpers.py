from __future__ import print_function

import datetime
from datetime import timedelta
from django.conf import settings
from rest_framework.pagination import PageNumberPagination

from rest_framework import status
from rest_framework.response import Response

from . import settings

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from twilio.rest import Client

import pickle
import random


# Pagination
PAGINATOR = PageNumberPagination()
PAGINATOR.page_size = 10
PAGINATOR_PAGE_SIZE = PAGINATOR.page_size


def get_object(model, pk):
    try:
        return model.objects.get(pk=pk)
    except model.DoesNotExist:
        return None


def custom_response(status_value, code, message, result={}):
    return Response({
        'status': status_value,
        'code': code,
        'message': message,
        'data': result
    }, status=status.HTTP_200_OK)


def dict_obj_list_to_str(data):
    for key, value in data.items():
        data[key] = "".join(value)
    return data


def get_pagination_response(model_class, request, serializer_class, context):
    result = {}
    model_response = PAGINATOR.paginate_queryset(model_class, request)
    serializer = serializer_class(model_response, many=True, context=context)
    result.update({'data': serializer.data})
    current = PAGINATOR.page.number
    next_page = 0 if PAGINATOR.get_next_link() is None else current + 1
    previous_page = 0 if PAGINATOR.get_previous_link() is None else current - 1
    result.update({'links': {
        'current': current,
        'next': next_page,
        'previous': previous_page,
        'total': PAGINATOR.page.paginator.count,
        'last': PAGINATOR.page.paginator.num_pages,
    }})
    return result


def serialized_response(serializer, message):
    if serializer.is_valid():
        serializer.save()
        result = serializer.data
        response_status = True
    else:
        result = dict_obj_list_to_str(serializer.errors)
        response_status = False
        message = "Please resolve error(s) OR fill Missing field(s)!"
    return response_status, result, message


def send_email(user, subject, text_content):
    from_email = 'druz2105@gmail.com'
    to = user.email
    message = Mail(
        from_email=from_email,
        to_emails=to,
        subject=subject,
        plain_text_content=text_content,
    )
    sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
    response = sg.send(message)
    return "Mail has been sent successfully"