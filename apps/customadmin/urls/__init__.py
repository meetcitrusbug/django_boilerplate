# -*- coding: utf-8 -*-
from django.urls import include, path

from .. import views
from django.views.generic import TemplateView
from . import url_core, urls_auth

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("", include(urls_auth)),
    path("", include(url_core)),
]