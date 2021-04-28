"""
This module works as a generic context data processor
throughout the App.
"""

from django.conf import settings


def settings_context(_request):
    """This function provides 'settings' context in the App"""
    return {"settings": settings}
