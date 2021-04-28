"""
You can import your all individual util functions here,

These imported functions can be directly accessible throughout the Application.

This __init__ file works same as a default __init__ method in any class OR function.
"""

import functools
from importlib import import_module

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured, ValidationError
from django.utils.module_loading import import_string
from rest_framework import status
from six import string_types

from .api import get_status, modify_api_response
from django_boilerplate.utils.core  import (
    admin_urlname,
    # filter_admin,
    # filter_channel_category,
    # filter_live_stream_category,
    # filter_perms,
    # filter_podcast_category,
    # filter_superadmin,
    # filter_vendor,
    get_deleted_objects,
)
from .emails import Emails
from .exception import CustomValidation
# from .order import (
#     create_charge_object,
#     create_card_object,
#     create_bank_object,
#     create_customer_id,
# )
# from .stripe import MyStripe
# from .twilio import send_sms
# from .validator import validate_date, validate_file_size

# ---------------------------------------------------------------------------------


def import_callable(path_or_callable):
    """This is used to import a callable module"""
    if hasattr(path_or_callable, '__call__'):
        return path_or_callable
    else:
        assert isinstance(path_or_callable, string_types)
        package, attr = path_or_callable.rsplit('.', 1)
        return getattr(import_module(package), attr)


def default_create_token(token_model, user, serializer):
    """Creates a new token if not available"""
    token, _ = token_model.objects.get_or_create(user=user)
    return token


def jwt_encode(user):
    """This method encodes the JWT of user"""
    try:
        from rest_framework_jwt.settings import api_settings
    except ImportError:
        raise ImportError("djangorestframework_jwt needs to be installed")

    jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
    jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

    payload = jwt_payload_handler(user)
    return jwt_encode_handler(payload)


@functools.lru_cache(maxsize=None)
def get_default_password_validators():
    """To get default password validator defined in the settings file"""
    return get_password_validators(settings.AUTH_PASSWORD_VALIDATORS)


def get_password_validators(validator_config):
    """Get list of password validators"""
    validators = []
    for validator in validator_config:
        try:
            klass = import_string(validator['NAME'])
        except ImportError:
            msg = "The module in NAME could not be imported: %s. Check your AUTH_PASSWORD_VALIDATORS setting."
            raise ImproperlyConfigured(msg % validator['NAME'])
        validators.append(klass(**validator.get('OPTIONS', {})))

    return validators


def validate_password(password, user=None, password_validators=None):
    """
    Validate whether the password meets all validator requirements.

    If the password is valid, return ``None``.
    If the password is invalid, raise ValidationError with all error messages.
    """
    errors = []
    if password_validators is None:
        password_validators = get_default_password_validators()
    for validator in password_validators:
        try:
            validator.validate(password, user)
        except ValidationError as error:
            errors.append(error)
    if errors:
        # raise ValidationError(errors)
        raise CustomValidation(
            "This password is too short. "
            "OR It must contain at least 8 characters. "
            "OR This password is too common. "
            "OR This password is entirely numeric.",
            status_code=status.HTTP_200_OK
        )
