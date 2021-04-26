from notification.models import GroupUser
from django import forms 


class CreateGroupUserForm(forms.ModelForm):
    
    class Meta:
        model = GroupUser
        fields = ['group_name', 'user']