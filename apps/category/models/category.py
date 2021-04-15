from django.db import models
from django_boilerplate.models import ActivityTracking
from django.utils.translation import ugettext_lazy as _


class Category(ActivityTracking):
    name = models.CharField(_('name'), max_length=255)
    image = models.ImageField(_('image'), upload_to='category_image')
    
    
    class Meta: 
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        
    def __str__(self):
        
        return self.name