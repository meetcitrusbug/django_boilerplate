from rest_framework.views import APIView
from .notification_serializer import NotificationSerializer
from .models import Notification
from django_boilerplate.helpers import custom_response, serialized_response, get_object
from rest_framework import status
from django_boilerplate.permissions import IsAccountOwner

from pyfcm import FCMNotification
from rest_framework.permissions import AllowAny
from django.conf import settings


class NotificationListView(APIView):
    """
    Fetch all notifications of given user
    """
    permission_classes = (AllowAny,)
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
    
    permission_classes = (AllowAny,)

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
    permission_classes = (AllowAny,)
    
    def post(self, request, format=None):
        Notification.objects.filter(is_read=False).update(is_read=True)
        message = "All Notifications Marked as Read Successfully!"            
        return custom_response(True, status.HTTP_200_OK, message)


class RemoveNotificationView(APIView):
    """
    Remove a given Notifications
    """
    permission_classes = (AllowAny,)
    
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
    permission_classes = (AllowAny,)
    
    def delete(self, request, format=None):
        Notification.objects.all().delete()
        # Notification.objects.filter(user=request.user).delete()
        message = "All Notifications removed Successfully!"            
        return custom_response(True, status.HTTP_200_OK, message)


class SendNotificationView(APIView):
    """
    Send Notifications
    """
    permission_classes = (AllowAny,)
    
    def post(self, request):
        api_key = settings.FIREBASE_API_KEY
        cred1 = "eURcBgsSckRFrYhgE-O7yo:APA91bF64RceddvQLvzOmUAqmp88PrneQN5m38L2ImSiLeQhdrT7k1qkDoea3v6nQx7tdJ3PJ6aJhKfvBlF_MZ01zkwF1AsVcYJft5ERaTVKRpBl3l_cCpJtiunO98gS__-aAcsh3CFM"
        # cred2 = "f1XwkdJ5TEZotso-s3BO_X:APA91bHCv5jeXfaMszcOan2MoU0pJTbzkVBifCW_tJ_p1hcprhzLAFOcuOT86g8Kk-48RZu5bKaSuhaq-Qk557ILKgJeW3Y6tuCSO54fWfFKGQTPTjGEStMB-nnOOqAPg_rUMBC8kOR4"

        credentials = [cred1]
        # credentials = [cred1, cred2]

        if len(credentials) > 1:
            push_service = FCMNotification(api_key=api_key)
            registration_ids = credentials

            message_title = "Citrusbug Notification API!"
            message_body = "Hope you're having fun this weekend, don't forget to check today's news"
            result = push_service.notify_multiple_devices(registration_ids=registration_ids, message_title=message_title, message_body=message_body)
            print(result, "============================")
        else:
            push_service = FCMNotification(api_key=api_key)
            for credential in credentials:
                registration_ids = credential

            message_title = "Citrusbug Notification API!"
            message_body = "Hi john, your customized news for today is ready"
            result = push_service.notify_single_device(registration_id=registration_ids, message_title=message_title, message_body=message_body)
            print(result, "============================")

        if result['success'] == 1:
            message = "Notification sent successfully!"          
            return custom_response(True, status.HTTP_200_OK, message)
        else:
            message = "Notification isn't sent successfully!"
            return custom_response(False, status.HTTP_200_OK, message)