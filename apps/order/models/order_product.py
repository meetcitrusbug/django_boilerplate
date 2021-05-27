from django.db import models
from django_boilerplate.models import ActivityTracking

class OrderProduct(ActivityTracking):
    
    order = models.ForeignKey('order.Order', on_delete=models.CASCADE)
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    amount  = models.PositiveIntegerField(default=0)