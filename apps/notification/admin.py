from django.contrib import admin
from .models import Notification, Group, GroupUser

class NotificationAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ["pk", "title", "is_read", 'is_singleuser', 'group', 'user']

class GroupAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ["pk", "group_name"]

class GroupUserAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ["pk", "group_name", "user"]

admin.site.register(Notification, NotificationAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(GroupUser, GroupUserAdmin)