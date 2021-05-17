# -*- coding: utf-8 -*-

from django import forms

from notification.models import Group, GroupUser


# -----------------------------------------------------------------------------
# Group
# -----------------------------------------------------------------------------

class GroupCreationForm(forms.ModelForm):
    """Custom GroupCreationForm"""

    class Meta():
        model = Group
        fields = [
            "group_name",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(GroupCreationForm, self).clean()
        group_name = cleaned_data.get("group_name")

        if not group_name :
            raise forms.ValidationError(
                "Please add a group name!."
            )
        
        if Group.objects.filter(group_name__iexact=group_name).exists():
            raise forms.ValidationError(
                "Group name already exists!"
            )

    def save(self, commit=True):
        instance = super().save(commit=False)

        if commit:
            instance.save()

        return instance


class GroupChangeForm(forms.ModelForm):
    """Custom form to change Group"""

    class Meta():
        model = Group

        fields = [
            "group_name",
        ]

    def clean(self):
        cleaned_data = super(GroupChangeForm, self).clean()
        group_name = cleaned_data.get("group_name")

        if not group_name :
            raise forms.ValidationError(
                "Please add group name!"
            )

    def save(self, commit=True):
        instance = super().save(commit=False)

        if commit:
            instance.save()

        return instance