"""
This is a validator module used to validate any field before storing it to the database.
"""

from django.core.exceptions import ValidationError
from django.utils import timezone


def validate_date(date):
    """This method validates the date field"""
    if date < timezone.now().date():
        raise ValidationError("Date cannot be in the past")


def validate_file_size(value):
    """This method validates the file size"""
    file_size = value.size

    if file_size > 20971520:
        raise ValidationError("The maximum file size that can be uploaded is 20 MB")
    else:
        return value
