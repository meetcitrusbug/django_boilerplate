from django.urls import path
from . import views

app_name='customadmin'

urlpatterns = [
    path("", views.IndexView.as_view(), name="dashboard"),
        # User
    path("users/", views.UserListView.as_view(), name="user-detail"),

    path("users/<int:pk>/detail/", views.UserDetailView.as_view(), name="user-detailview"),
    path("users/", views.UserListView.as_view(), name="user-list"),
    path("users/create/", views.UserCreateView.as_view(), name="user-create"),
    path("users/<int:pk>/update/", views.UserUpdateView.as_view(), name="user-update"),
    path("users/<int:pk>/delete/", views.UserDeleteView.as_view(), name="user-delete"),
    path("users/<int:pk>/password/", views.UserPasswordView.as_view(), name="user-password"),
    path("ajax-users", views.UserAjaxPagination.as_view(), name="user-list-ajax"),

    path("export_user_csv", views.export_user_csv, name="export_user_csv"),
]

urlpatterns +=[
#------------------------------------------------------------------------------------------------------
   #Blog
    path("blog/", views.BlogListView.as_view(), name="blog-list"),
    path("blog/create/", views.BlogCreateView.as_view(), name="blog-create"),
    path("blog/<int:pk>/update/", views.BlogUpdateView.as_view(), name="blog-update"),
    path("blog/<int:pk>/delete/", views.BlogDeleteView.as_view(), name="blog-delete"),
    path("ajax-blog", views.BlogAjaxPagination.as_view(), name="blog-list-ajax"),

#------------------------------------------------------------------------------------------------------
   #BlogKeyword
    path("blogkeyword/", views.BlogKeywordListView.as_view(), name="blogkeyword-list"),
    path("blogkeyword/create/", views.BlogKeywordCreateView.as_view(), name="blogkeyword-create"),
    path("blogkeyword/<int:pk>/update/", views.BlogKeywordUpdateView.as_view(), name="blogkeyword-update"),
    path("blogkeyword/<int:pk>/delete/", views.BlogKeywordDeleteView.as_view(), name="blogkeyword-delete"),
    path("ajax-blogkeyword", views.BlogKeywordAjaxPagination.as_view(), name="blogkeyword-list-ajax"),

#------------------------------------------------------------------------------------------------------
   #Category
    path("category/", views.CategoryListView.as_view(), name="category-list"),
    path("category/create/", views.CategoryCreateView.as_view(), name="category-create"),
    path("category/<int:pk>/update/", views.CategoryUpdateView.as_view(), name="category-update"),
    path("category/<int:pk>/delete/", views.CategoryDeleteView.as_view(), name="category-delete"),
    path("ajax-category", views.CategoryAjaxPagination.as_view(), name="category-list-ajax"),
]