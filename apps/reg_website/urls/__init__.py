from django.urls import include, path
from . import user_auth_urls, user_profile_urls

app_name="reg_website"

urlpatterns = [
    path("", include(user_auth_urls)),
    path("", include(user_profile_urls)),
]