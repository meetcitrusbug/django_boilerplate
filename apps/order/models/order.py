from django.db import models

from django_boilerplate.models import ActivityTracking

class Order(ActivityTracking):
    
    STATUS_CHOICES = (
        ('PLACED','PLACED'),
        ('PENDING','PENDING'),
        ('SHIPPING','SHIPPING'),
        ('COMPLETED','COMPLETED'),
        ('CANCELLED','CANCELLED'),
    )
    BASE_VALUE = 1000
    
    order_id = models.IntegerField(null=True, blank=True)
    transaction_id = models.CharField(max_length=500)    
    user = models.ForeignKey('django_boilerplate.User', on_delete=models.CASCADE)
    card = models.ForeignKey('order.UserCard', on_delete=models.SET_NULL,
                                        null=True)
    total_amount = models.PositiveIntegerField()
    status = models.CharField(max_length=20, default='PLACED', choices=STATUS_CHOICES)
    billing_address = models.ForeignKey('order.Address', on_delete=models.SET_NULL,
                                        null=True, related_name='billing_address')
    shipping_address = models.ForeignKey('order.Address', on_delete=models.SET_NULL,
                                        null=True, related_name='shipping_address') 

    def __str__(self):
        return f'{self.pk}' 
    
    class Meta:
        verbose_name='Order'
        verbose_name_plural='Orders'
        
    def save(self, *args, **kwargs):
        instance = super().save(*args, **kwargs)   
        order = Order.objects.filter(pk=self.pk).update(
         order_id = self.BASE_VALUE+self.pk   
        )
        return instance