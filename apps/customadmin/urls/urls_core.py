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
   #Group
    path("group/", views.GroupListView.as_view(), name="group-list"),
    path("group/create/", views.GroupCreateView.as_view(), name="group-create"),
    path("group/<int:pk>/update/", views.GroupUpdateView.as_view(), name="group-update"),
    path("group/<int:pk>/delete/", views.GroupDeleteView.as_view(), name="group-delete"),
    path("ajax-group", views.GroupAjaxPagination.as_view(), name="group-list-ajax"),

    #------------------------------------------------------------------------------------------------------
   #GroupUser
    path("groupuser/", views.GroupUserListView.as_view(), name="groupuser-list"),
    path("groupuser/create/", views.GroupUserCreateView.as_view(), name="groupuser-create"),
    path("groupuser/<int:pk>/update/", views.GroupUserUpdateView.as_view(), name="groupuser-update"),
    path("groupuser/<int:pk>/delete/", views.GroupUserDeleteView.as_view(), name="groupuser-delete"),
    path("ajax-groupuser", views.GroupUserAjaxPagination.as_view(), name="groupuser-list-ajax"),

#------------------------------------------------------------------------------------------------------
   #Notification
    path("notification/<int:pk>/detail/", views.NotificationDetailView.as_view(), name="notification-detailview"),
    path("notification/", views.NotificationListView.as_view(), name="notification-list"),
    path("notification/create/", views.NotificationCreateView.as_view(), name="notification-create"),
    path("notification/<int:pk>/update/", views.NotificationUpdateView.as_view(), name="notification-update"),
    path("notification/<int:pk>/delete/", views.NotificationDeleteView.as_view(), name="notification-delete"),
    path("ajax-notification", views.NotificationAjaxPagination.as_view(), name="notification-list-ajax"),
    path('notification-send/', views.NotificationSendView.as_view(), name='notification-send'),

#------------------------------------------------------------------------------------------------------
   #UserNotification
    path("usernotification/", views.UserNotificationListView.as_view(), name="usernotification-list"),
    path("usernotification/create/", views.UserNotificationCreateView.as_view(), name="usernotification-create"),
    path("usernotification/<int:pk>/update/", views.UserNotificationUpdateView.as_view(), name="usernotification-update"),
    path("usernotification/<int:pk>/delete/", views.UserNotificationDeleteView.as_view(), name="usernotification-delete"),
    path("ajax-usernotification", views.UserNotificationAjaxPagination.as_view(), name="usernotification-list-ajax"),

]