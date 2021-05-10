from django.db import models

# Create Category Model for blog
class Category(models.Model):
    category = models.CharField(max_length=128,blank=True,null=True)

    def __str__(self):
        return self.category