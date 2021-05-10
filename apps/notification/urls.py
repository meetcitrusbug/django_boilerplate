from django.urls import path
from . import views

# app_name = 'notification'
urlpatterns = [
    path('notification/notification-list/', views.NotificationListView.as_view(), name='notification-list'),
    path('notification/read/<int:pk>/', views.ReadNotificationView.as_view(), name='notification-read'),
    path('notification/read/', views.ReadAllNotificationView.as_view(), name='notifications-read-all'),
    path('notification/remove/<int:pk>/', views.RemoveNotificationView.as_view(), name='notifications-read'),
    path('notification/remove/', views.RemoveAllNotificationView.as_view(), name='notifications-read-all'),
    path('notification/send/', views.SendNotificationView.as_view(), name='send-notifications'),
]