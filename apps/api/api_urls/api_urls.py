from django.urls import path
from django.conf.urls import url
from .. import api_views as views

urlpatterns = [
    path('blogs/',views.BlogListView.as_view(),name='blogs'),
    path('blog/<str:id>/',views.BlogDetailView.as_view(),name='blog-detail'),
    path('add-blog',views.BlogCreateView.as_view(),name='blog-create'),
    path('edit-blog/<str:id>/',views.BlogUpdateView.as_view(),name='blog-update'),
    path('delete-blog/<str:id>/',views.BlogDeleteView.as_view(),name='blog-delete'),
]