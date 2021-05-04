# -*- coding: utf-8 -*-

from django import forms

from notification.models import UserNotification


# -----------------------------------------------------------------------------
# UserNotification
# -----------------------------------------------------------------------------

class UserNotificationCreationForm(forms.ModelForm):
    """Custom UserNotificationCreationForm"""

    class Meta():
        model = UserNotification
        fields = [
            "user",
            "notification",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(UserNotificationCreationForm, self).clean()
        user = cleaned_data.get("user")
        notification = cleaned_data.get("notification")

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
        return instance


class UserNotificationChangeForm(forms.ModelForm):
    """Custom form to change UserNotification"""

    class Meta():
        model = UserNotification
        fields = [
            "user",
            "notification",
        ]

    def clean(self):
        cleaned_data = super(GroupChangeForm, self).clean()
        user = cleaned_data.get("user")
        notification = cleaned_data.get("notification")

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
        return instance