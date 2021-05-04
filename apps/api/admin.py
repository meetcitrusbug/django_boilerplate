from django.contrib import admin
from . models import User


class UserAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ["pk", "username", "apple_token", 'email', 'is_staff']


admin.site.register(User, UserAdmin)