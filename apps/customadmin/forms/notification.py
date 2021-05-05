# -*- coding: utf-8 -*-

from django import forms

from notification.models import Notification


# -----------------------------------------------------------------------------
# Notification
# -----------------------------------------------------------------------------

class NotificationCreationForm(forms.ModelForm):
    """Custom Notification"""

    class Meta():
        model = Notification
        fields = [
            "title",
            "description",
            "is_read",
            "is_singleuser",
            "group",
            "user",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(NotificationCreationForm, self).clean()
        title = cleaned_data.get("title")
        description = cleaned_data.get("description")
        is_read = cleaned_data.get("is_read")
        is_singleuser = cleaned_data.get("is_singleuser")
        group = cleaned_data.get("group")
        user = cleaned_data.get("user")

        if not title :
            raise forms.ValidationError(
                "Please add title!."
            )
        if not description :
            raise forms.ValidationError(
                "Please add description!"
            )
        if not is_singleuser :
            if not group:
                raise forms.ValidationError(
                    "Please select a group!"
                )
            self.cleaned_data['user'] = None
        if is_singleuser :
            if not user:
                raise forms.ValidationError(
                    "Please select a user!"
                )
            self.cleaned_data['group'] = None

    def save(self, commit=True):
        instance = super().save(commit=False)

        if commit:
            instance.save()

        return instance


class NotificationChangeForm(forms.ModelForm):
    """Custom form to change GroupUser"""

    class Meta():
        model = Notification

        fields = [
            "title",
            "description",
            "is_read",
            "is_singleuser",
            "group",
            "user",
        ]

    def clean(self):
        cleaned_data = super(NotificationChangeForm, self).clean()
        title = cleaned_data.get("title")
        description = cleaned_data.get("description")
        is_read = cleaned_data.get("is_read")
        is_singleuser = cleaned_data.get("is_singleuser")
        group = cleaned_data.get("group")
        user = cleaned_data.get("user")

        if not title :
            raise forms.ValidationError(
                "Please add title!."
            )
        if not description :
            raise forms.ValidationError(
                "Please add description!"
            )
        if not is_singleuser :
            if not group:
                raise forms.ValidationError(
                    "Please select a group!"
                )
            self.cleaned_data['user'] = None
        if is_singleuser :
            if not user:
                raise forms.ValidationError(
                    "Please select a user!"
                )
            self.cleaned_data['group'] = None

    def save(self, commit=True):
        instance = super().save(commit=False)

        if commit:
            instance.save()

        return instance