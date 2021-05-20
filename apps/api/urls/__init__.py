from django.urls import include, path
from . import user_urls_api, profile_urls_api

app_name = 'api'

urlpatterns = [
    path('',include(user_urls_api)),
    path('',include(profile_urls_api)),
]