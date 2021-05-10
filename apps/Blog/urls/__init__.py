from django.urls import path, include
from .. import views
from . import blog

urlpatterns = [
    path("", include(blog)),

]