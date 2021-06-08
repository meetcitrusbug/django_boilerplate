from django.contrib import admin
from .models import Blog, Category, BlogKeyword
# Register your models here.
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['id','blog_title']
    list_per_page = 10

@admin.register(BlogKeyword)
class BlogKeywordAdmin(admin.ModelAdmin):
    list_display = ['id','keyword']
    list_per_page = 10

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','category']
