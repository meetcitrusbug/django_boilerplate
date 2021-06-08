from django.urls import path
from django.conf.urls import url
from Blog import views

urlpatterns = [
    path('',views.BlogListingView.as_view(),name='blog-listing'),
    path('createblog',views.CreateBlogView.as_view(),name='create-blog'),
    path('blogdetail/<str:blog_id>',views.BlogDetailView.as_view(),name='blog-detail'),
    path('blogupdate/<str:blog_id>',views.BlogUpdateView.as_view(),name='blog-update'),
    path('blog-search/',views.BlogSearchView.as_view(),name='blog-search'),
    path('login',views.LoginPageView.as_view(),name='login'),
    path('logout',views.userlogout,name='logout'),
]