from django.db import models
from datetime import datetime
from.category import Category
from django_boilerplate.models import User, ActivityTracking

# Create your models here.
class Blog(ActivityTracking):
    blog_title = models.CharField(max_length=128)
    blog = models.TextField()
    image = models.ImageField(default=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,blank=True,null=True)
    author = models.CharField(max_length=128,blank=True,null=True)
    user = models.ForeignKey("django_boilerplate.User",null=True,blank=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.blog_title

class BlogKeyword(models.Model):
    blog = models.ForeignKey("Blog",on_delete=models.CASCADE,blank=True,null=True)
    keyword = models.CharField(max_length=55,null=True,blank=True)

    def __str__(self):
        return self.keyword
