from notification.models import Group
from django import forms 


class CreateGroupForm(forms.ModelForm):
    
    class Meta:
        model = Group
        fields = ['group_name']