from django.urls import path
from django.conf.urls import url
from Blog import api_views as views

urlpatterns = [
    path('blogs/',views.BlogListView,name='blogs'),
    path('blog/<str:blog_id>/',views.BlogDetailView,name='blog-detail'),
    path('add-blog',views.BlogCreateView,name='blog-create'),
    path('edit-blog/<str:blog_id>/',views.BlogUpdateView,name='blog-update'),
    path('delete-blog/<str:blog_id>/',views.BlogDeleteView,name='blog-delete'),
]