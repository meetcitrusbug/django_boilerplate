from django.db import models

# Create Author Model for blog
class Author(models.Model):
    name = models.CharField(max_length=128,blank=True,null=True)

    def __str__(self):
        return self.name