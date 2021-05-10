from django.db import models
from datetime import datetime
from.category import Category
from.author import Author
# Create your models here.
class Blog(models.Model):
    blog_title = models.CharField(max_length=128)
    blog = models.TextField(max_length=200)
    keyword = models.CharField(max_length=55,null=True,blank=True)
    publish = models.DateTimeField(default=datetime.now(),blank=True)
    image = models.ImageField(default=True)
    language = models.CharField(max_length=128,blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,blank=True,null=True)
    author = models.ForeignKey(Author,on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return self.blog_title
