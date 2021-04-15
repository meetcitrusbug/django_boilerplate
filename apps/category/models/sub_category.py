from django.db import models
from django_boilerplate.models import ActivityTracking
from django.utils.translation import ugettext_lazy as _


class SubCategory(ActivityTracking):
    name = models.CharField(_('name'), max_length=255)
    image = models.ImageField(_('image'), upload_to='category_image')
    category = models.ForeignKey('category.Category', on_delete=models.CASCADE)
    
    class Meta: 
        verbose_name = "SubCategory"
        verbose_name_plural = "SubCategories"
        
    def __str__(self):
        
        return self.name