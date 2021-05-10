from django.urls import  path, include

urlpatterns = [
    path('',include('Blog.api_urls'))
]