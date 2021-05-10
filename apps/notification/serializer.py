from rest_framework import fields, serializers
from .models import Notification
from customadmin.models import User


class NotificationUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')

class NotificationSerializer(serializers.ModelSerializer):
    user = NotificationUserSerializer()
    class Meta:
        model = Notification
        fields = ('id', 'title', 'description', 'user', 'is_read', 'created_at', 'is_singleuser', 'group', 'user')