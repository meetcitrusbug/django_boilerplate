from rest_framework import fields, serializers
from .models import Notification
# from .models import Notification, User


# class NotificationUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'email', 'profile_image')

class NotificationSerializer(serializers.ModelSerializer):
    # user = NotificationUserSerializer()
    class Meta:
        model = Notification
        fields = ('id', 'title', 'description', 'notification_type', 'is_read', 'created_at', 'profile_image', 'is_singleuser', 'status', 'group', 'user')
        # fields = ('id', 'title', 'description', 'user', 'notification_type', 'is_read', 'created_at')
