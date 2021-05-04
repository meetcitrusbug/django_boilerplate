from rest_framework.views import APIView
from .notification_serializer import NotificationSerializer
from .models import Notification
from django_boilerplate.helpers import custom_response, serialized_response, get_object
from rest_framework import status
from django_boilerplate.permissions import IsAccountOwner

from pyfcm import FCMNotification


class NotificationListView(APIView):
    """
    Fetch all notifications of given user
    """
    permission_classes = (IsAccountOwner,)
    serializer_class = NotificationSerializer

    def get(self, request):
        notifications = Notification.objects.all().order_by('-id')
        serializer = self.serializer_class(notifications, many=True, context= {"request": request})
        result={}
        result['notifications'] = serializer.data
        result['unread_count'] = Notification.objects.filter(is_read=False).count()
        message = "Notifications fetched successfully!"
        return custom_response(True, status.HTTP_200_OK, message, result)


class ReadNotificationView(APIView):
    """
    Mark given Notifications as read
    """
    
    permission_classes = (IsAccountOwner,)

    def post(self, request, pk, format=None):
        notification = get_object(Notification, pk)
        if not notification:
            message = "Notification not found!"
            return custom_response(False, status.HTTP_400_BAD_REQUEST, message)
        notification.is_read = True
        notification.save()
        message = "Notification Marked as Read Successfully!"
        return custom_response(True, status.HTTP_200_OK, message)


class ReadAllNotificationView(APIView):
    """
    Mark all Notifications as read
    """
    permission_classes = (IsAccountOwner,)
    
    def post(self, request, format=None):
        Notification.objects.filter(is_read=False).update(is_read=True)
        message = "All Notifications Marked as Read Successfully!"            
        return custom_response(True, status.HTTP_200_OK, message)


class RemoveNotificationView(APIView):
    """
    Remove a given Notifications
    """
    permission_classes = (IsAccountOwner,)
    
    def delete(self, request, pk, format=None):
        notification = get_object(Notification, pk)
        if not notification:
            message = "Notification not found!"
            return custom_response(False, status.HTTP_400_BAD_REQUEST, message)
        notification.delete()
        message = "Notification Deleted Successfully!"
        return custom_response(True, status.HTTP_200_OK, message)


class RemoveAllNotificationView(APIView):
    """
    Remove all Notifications
    """
    permission_classes = (IsAccountOwner,)
    
    def delete(self, request, format=None):
        Notification.objects.all().delete()
        message = "All Notifications removed Successfully!"            
        return custom_response(True, status.HTTP_200_OK, message)


class SendNotificationView(APIView):
    """
    Send Notifications
    """
    permission_classes = (IsAccountOwner,)
    
    def post(self, request):
        api_key = "AAAA-F3kDws:APA91bENHxS72ai1So4PXQ1htHc2XhApysw_KksmyQWWy_aZe-Pq_-BrVP4yxY3dG452oPt3YLGzecjhLGL0ufs3rELk0Gidq9ZamPwl7caLyWKewE-3Vpv1EYKpBmmdv_EzrqxkLjeR"
        credentials = ["<device registration_id 1>", "<device registration_id 1>"]

        if len(credentials) > 1:
            push_service = FCMNotification(api_key=api_key)
            registration_ids = credentials

            message_title = "Citrusbug update!"
            message_body = "Hope you're having fun this weekend, don't forget to check today's news"
            result = push_service.notify_multiple_devices(registration_ids=registration_ids, message_title=message_title, message_body=message_body)
        else:
            push_service = FCMNotification(api_key=api_key)
            for credential in credentials:
                registration_ids = credential

            message_title = "Citrusbug update!"
            message_body = "Hi john, your customized news for today is ready"
            result = push_service.notify_single_device(registration_id=registration_ids, message_title=message_title, message_body=message_body)

        if result['success'] == 1:
            message = "Notification sent successfully!"          
            return custom_response(True, status.HTTP_200_OK, message)
        else:
            message = "Notification isn't sent successfully!"
            return custom_response(False, status.HTTP_200_OK, message)