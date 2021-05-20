from django import forms
from ..models import User


class SignUpForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'username'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'first_name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'last_name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'id': 'email'}))
    phone_no = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control col-12', 'id': 'phone'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'password'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'confirm_password'}))
