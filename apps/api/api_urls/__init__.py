from django.urls import path, include
from .. import views
from . import api_urls

urlpatterns = [
    path("", include(api_urls)),

]