import uuid
from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import AbstractUser

class ActivityTracking(models.Model):
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True, verbose_name='is active')
    
    class Meta:
        abstract = True
        
class User(AbstractUser):
    email = models.EmailField(null=True, blank=True, unique=True)
    username = models.CharField(max_length=40, blank=True, null=True,default='')
    first_name = models.CharField(max_length=40, blank=True)
    last_name = models.CharField(max_length=40, blank=True)
    profile_image = models.ImageField(upload_to="profile_image", null=True,  blank=True, verbose_name=_("Profile Image"))
    credentials = models.CharField(max_length=200, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"