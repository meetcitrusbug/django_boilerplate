# -*- coding: utf-8 -*-
"""
This is the module where you can get the status code of
the API response & you can also modify the API response format.
"""

from rest_framework import status
from rest_framework.authtoken.models import Token
import datetime
from django.utils import timezone
from django.conf import settings
from dateutil.relativedelta import relativedelta
# from core import models
# from core import api
from rest_framework import status
# from core.api import serializers

# -----------------------------------------------------------------------------


def get_status(code):
    """Get the human readable SNAKE_CASE version of a status code."""
    for name, val in status.__dict__.items():
        if not callable(val) and code is val:
            return name.replace("HTTP_%s_" % code, "")
    return "UNKNOWN"

def modify_api_response(response):
    """
    Modify API response format.
    Example success:
    {
        "code": 200,
        "status": "OK",
        "data": {
            "username": "username"
        }
    }

    Example error:
    {
        "code": 404,
        "status": "NOT_FOUND",
        "errors": [
            {
                "title": "detail",
                "detail": "Not found."
            }
        ]
    }
    """
    # # If errors we got this from the exception handler which already modified the response
    # if status.is_client_error(response.status_code) or status.is_server_error(
    #     response.status_code
    # ):
    #     return response

    # Modify the response data
    modified_data = {}
    modified_data["code"] = response.status_code
    # modified_data["status"] = get_status(response.status_code)

    if response.data.get("errors"):
        modified_data["status"] = False
        modified_data["message"] = response.data.get("errors")[0].get("detail")
        modified_data["data"] = []
        # modified_data["errors"] = response.data.get("errors")

    else:
        if response.data.get("status") is None:
            modified_data["status"] = True
        else:
            modified_data["status"] = response.data.get("status")
        modified_data["message"] = response.data.get("message")
        modified_data["data"] = response.data.get("data")

    response.data = modified_data
    return response

# def to_representation(user):  
        
#         if user:
#             token, created = Token.objects.get_or_create(user=user)
#             from core.api.serializers import LanguageSerializer
#             serializer  = LanguageSerializer(user.language)
#             return {
#                 "id": user.id,
#                 "email": user.email,
#                 "name": user.name,
#                 "instructor": user.instructor,
#                 "download_quality":user.download_quality,
#                 "train_time":user.train_time,
#                 "focus_topic":get_focus_topic(user),
#                 "pause_length":user.pause_length,
#                 "new_user":user.new_user,
#                 "token": f"Token {token.key}",
#                 "langugage":serializer.data,
#                 "trail_expired": is_trial_expired(user),
#                 "subscription_over": check_subscription(user),
#                 "personal_program:":personal_program(user),
#             }
#         return {}
 
# def is_trial_expired(user, with_message=False):
    
#     """
#         Check user's trail period is over or not
#     """
    
#     subscription = models.Subscription.objects.filter(user=user).first()
#     invitation = models.ShareProgramEmail.objects.filter(
#                 user=user, accept=True
#     ).order_by('-created_at', '-share_program__free_month').first()
      
#     return_data = {
#         'flag':False,
#         'message':''
#     }
    
#     if subscription:  
#         #     
#         # checking that user already have subscription or not
#         #
#         return_data['flag'] = False
        
#     elif invitation:
#         #
#         # checking user's is invited for some program and for how many months 
#         # and those months are passed since user accepted that invitation
#         #
#         invitation_date_expire = invitation.accept_date  + relativedelta(
#                                 months=invitation.share_program.free_month)
#         flag =  invitation_date_expire < timezone.now()
        
#         if flag:
#             return_data['flag'] = flag
#             return_data['message'] = "%s months has been over since you invited for some program" % invitation.share_program.free_month

#     else:   
#         #     
#         # check trail expiration since user join the app
#         #
#         join_date =  user.join_date + datetime.timedelta(days=settings.TRIAL_DAYS)
#         flag = join_date < timezone.now()
#         return_data['flag'] = flag
#         return_data['message'] = "Your trial is finished! to continue you have to take subscription"
        
#     if with_message :
#         return return_data
    
#     return return_data['flag']

# def get_focus_topic(user):
#     if user.focus_topic:
#         return api.serializers.FocusTopicListSerializer(
#             user.focus_topic).data
#     return {}

# def check_subscription(user):
#     return not models.Subscription.objects.filter(user=user).exists()


# def personal_program(user):
    
#     my_program = models.MyProgram.objects.filter(user=user, program__public=True).first()
    
#     if not my_program:
#         return {}
    
#     if not my_program.program:
#         return {}
    
#     return {
#         "id":my_program.program.id,
#         "name":my_program.program.name,
#     }