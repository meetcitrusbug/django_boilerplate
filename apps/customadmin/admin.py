from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .forms import AccountUpdateForm, AccountCreationForm
from django.utils.translation import ugettext_lazy as _
