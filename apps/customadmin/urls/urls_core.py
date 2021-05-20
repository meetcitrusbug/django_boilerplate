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
    # MediaCategory
    path("mediacategory/", views.MediaCategoryListView.as_view(), name="mediacategory-list"),
    path("mediacategory/create/", views.MediaCategoryCreateView.as_view(), name="mediacategory-create"),
    path("mediacategory/<int:pk>/update/", views.MediaCategoryUpdateView.as_view(), name="mediacategory-update"),
    path("mediacategory/<int:pk>/delete/", views.MediaCategoryDeleteView.as_view(), name="mediacategory-delete"),
    path("ajax-mediacategory", views.MediaCategoryAjaxPagination.as_view(), name="mediacategory-list-ajax"),
    
    #------------------------------------------------------------------------------------------------------
    # MediaImage
    path("mediaimage/", views.MediaImageListView.as_view(), name="mediaimage-list"),
    path("mediaimage/create/", views.MediaImageCreateView.as_view(), name="mediaimage-create"),
    path("mediaimage/<int:pk>/update/", views.MediaImageUpdateView.as_view(), name="mediaimage-update"),
    path("mediaimage/<int:pk>/delete/", views.MediaImageDeleteView.as_view(), name="mediaimage-delete"),
    path("ajax-mediaimage", views.MediaImageAjaxPagination.as_view(), name="mediaimage-list-ajax"),

    #------------------------------------------------------------------------------------------------------
    # MediaVideo
    path("mediavideo/", views.MediaVideoListView.as_view(), name="mediavideo-list"),
    path("mediavideo/create/", views.MediaVideoCreateView.as_view(), name="mediavideo-create"),
    path("mediavideo/<int:pk>/update/", views.MediaVideoUpdateView.as_view(), name="mediavideo-update"),
    path("mediavideo/<int:pk>/delete/", views.MediaVideoDeleteView.as_view(), name="mediavideo-delete"),
    path("ajax-mediavideo", views.MediaVideoAjaxPagination.as_view(), name="mediavideo-list-ajax"),
]