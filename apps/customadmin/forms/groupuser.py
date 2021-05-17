# -*- coding: utf-8 -*-

from django import forms

from notification.models import GroupUser


# -----------------------------------------------------------------------------
# GroupUser
# -----------------------------------------------------------------------------

class GroupUserCreationForm(forms.ModelForm):
    """Custom GroupUserCreationForm"""
    class Meta():
        model = GroupUser
        fields = [
            "group_name",
            "user",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(GroupUserCreationForm, self).clean()
        group_name = cleaned_data.get("group_name")
        user = cleaned_data.get("user")

        if not group_name :
            raise forms.ValidationError(
                "Please add a group name!."
            )
        if not user :
            raise forms.ValidationError(
                "Please add a user!"
            )
        if GroupUser.objects.filter(group_name=group_name, user=user).exists():
            raise forms.ValidationError(
                f"{user} is already exist in this {group_name}!"
            )


    def save(self, commit=True):
        cleaned_data = super(GroupUserCreationForm, self).clean()
        group_name = cleaned_data.get("group_name")
        user = cleaned_data.get("user")
        instance = None
        groupuser = GroupUser()
        if not GroupUser.objects.filter(group_name=group_name, user=user).exists():
            groupuser.group_name = group_name
            groupuser.user = user
            groupuser.save()
            instance = groupuser
        return instance

class GroupUserChangeForm(forms.ModelForm):
    """Custom form to change GroupUser"""

    class Meta():
        model = GroupUser

        fields = [
            "group_name",
            "user",
        ]

    def clean(self):
        cleaned_data = super(GroupUserChangeForm, self).clean()
        group_name = cleaned_data.get("group_name")
        user = cleaned_data.get("user")

        if not group_name :
            raise forms.ValidationError(
                "Please add a group name!"
            )
        if not user:
            raise forms.ValidationError(
                "Please add a user!"
            )

    def save(self, commit=True):
        cleaned_data = super(GroupUserChangeForm, self).clean()
        group_name = cleaned_data.get("group_name")
        user = cleaned_data.get("user")
        instance = None
        groupuser = GroupUser()
        if not GroupUser.objects.filter(group_name=group_name, user=user).exists():
            groupuser.group_name = group_name
            groupuser.user = user
            groupuser.save()
            instance = groupuser
        return instance