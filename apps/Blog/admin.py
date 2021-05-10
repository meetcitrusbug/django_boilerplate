from django.contrib import admin
from .models import Blog, Category, Author
# Register your models here.
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['id','blog_title','publish']
    list_per_page = 10

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','category']

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id','name']