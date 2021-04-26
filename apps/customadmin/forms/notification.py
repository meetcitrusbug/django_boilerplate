from notification.models import Notification
from django import forms 


class CreateNotificationForm(forms.ModelForm):
    class Meta:
        model = Notification
        fields = ['title', 'description', 'is_read', 'notification_type', 'profile_image', 'is_singleuser', 'status', 'group', 'user']