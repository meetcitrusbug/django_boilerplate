from rest_framework import fields, serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ('id', 'title', 'description', 'notification_type', 'is_read', 'created_at', 'profile_image', 'is_singleuser', 'status', 'group', 'user')
