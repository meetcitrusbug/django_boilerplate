from django.db import models

class ActivityTracking(models.Model):
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True, verbose_name='is active')
    
    class Meta:
        abstract = True