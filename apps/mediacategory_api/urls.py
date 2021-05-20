from django.urls import path
from . import views

urlpatterns = [
    path('mediacategory-list/', views.MediaCategoryListAPIView.as_view(), name="mediacategory-list-api"),
    path('mediacategory-detail/<int:id>/', views.MediaCategoryDetailAPIView.as_view(), name="mediacategory-detail-api"),
    path('mediacategory-create/', views.MediaCategoryCreateAPIView.as_view(), name="mediacategory-create-api"),
    path('mediacategory-update/<int:id>/', views.MediaCategoryUpdateAPIView.as_view(), name="mediacategory-update-api"),
    path('mediacategory-delete/<int:id>/', views.MediaCategoryDeleteAPIView.as_view(), name="mediacategory-delete-api"),
]

urlpatterns +=[
    path('mediaimage-create/', views.MediaImageAddAPIView.as_view(), name='mediaimage-create-api'),
    path('mediaimage-delete/<int:id>/', views.MediaImageDeleteAPIView.as_view(), name="mediaimage-delete-api"),

    path('mediavideo-create/', views.MediaVideoAddAPIView.as_view(), name='mediavideo-create-api'),
    path('mediavideo-delete/<int:id>/', views.MediaVideoDeleteAPIView.as_view(), name="mediavideo-delete-api"),
]