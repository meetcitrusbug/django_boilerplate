from django.db import models
from django_boilerplate.models import ActivityTracking
from django.utils.translation import ugettext_lazy as _


class ProductImage(ActivityTracking):
    
    image=  models.ImageField(_('image'), upload_to="product_image")
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE)
    
    class Meta: 
        verbose_name = "Product image"
        verbose_name_plural = "Product images"
        
    def __str__(self):
        
        return self.product.name