from django.db import models
from django_boilerplate.models import ActivityTracking

class Address(ActivityTracking):
    
    ADDRESS_CHOICES = (
        ('BILLING','BILLING'),
        ('SHIPPING','SHIPPING')
    )
    
    street = models.TextField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    type = models.CharField(max_length=10, choices=ADDRESS_CHOICES)
    
    
    def __str__(self):
        return f'{self.street}'
    
    def get_full_address(self):
        return f'{self.street}, {self.city}, {self.state}, {self.country}'