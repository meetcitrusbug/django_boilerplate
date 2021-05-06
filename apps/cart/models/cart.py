from django.db import models
from apps.utils.get_user_model import get_user_model
from django.utils.translation import ugettext_lazy as _
from django_boilerplate.models import ActivityTracking

class Cart(ActivityTracking):
    
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, db_index=True)
    product =  models.ForeignKey('product.Product', on_delete=models.CASCADE, db_index=True)
    quantity = models.PositiveIntegerField(_('Quantity'), default=0)
    
    def __str__(self):
        return '{}'.format(self.user)
    
    class Meta:
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'