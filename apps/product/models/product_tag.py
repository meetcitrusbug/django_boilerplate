from django.db import models
from django.utils.translation import ugettext_lazy as _

class ProductTag(models.Model):
    
    tag = models.CharField(_('tag'), max_length=300)
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE)

    def __str__(self):    
        return self.tag
    
    class Meta:
        verbose_name = "Product tag"
        verbose_name_plural = "Product tags"