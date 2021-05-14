from django.contrib import admin
from django_boilerplate.models import User


class UserModelAdmin(admin.ModelAdmin):
    
    model = User
    list_display = [ 'id', 'email', 'username', 'first_name', 'last_name']
        
admin.site.register(User, UserModelAdmin)