from . import views
from django.urls import path

urlpatterns = [
        path('', views.NotificationListView.as_view(), name="notification-list"),
        path('add-notification/', views.AddNotificationView.as_view(), name='add-notification'),
        path('edit-notification/<int:pk>', views.EditNotificationView.as_view(), name='edit-notification'),
        path('delete-notification/<int:pk>', views.DeleteNotificationView.as_view(), name='delete-notification'),
        path('notification-ajax', views.NotificationDataTablesAjaxPagination.as_view(), name='notification-list-ajax'),
        path('notification-send/<int:pk>', views.NotificationSendView.as_view(), name='notification-send'),
        
        path('group', views.GroupListView.as_view(), name="group-list"),
        path('add-group/', views.AddGroupView.as_view(), name='add-group'),
        path('edit-group/<int:pk>', views.EditGroupView.as_view(), name='edit-group'),
        path('delete-group/<int:pk>', views.DeleteGroupView.as_view(), name='delete-group'),
        path('group-ajax', views.GroupDataTablesAjaxPagination.as_view(), name='group-list-ajax'),

        path('groupuser', views.GroupUserListView.as_view(), name="groupuser-list"),
        path('add-groupuser/', views.AddGroupUserView.as_view(), name='add-groupuser'),
        path('edit-groupuser/<int:pk>', views.EditGroupUserView.as_view(), name='edit-groupuser'),
        path('delete-groupuser/<int:pk>', views.DeleteGroupUserView.as_view(), name='delete-groupuser'),
        path('groupuser-ajax', views.GroupUserDataTablesAjaxPagination.as_view(), name='groupuser-list-ajax'),
    ]