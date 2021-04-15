from django.contrib import admin
from . import models

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'image', 'is_active']    
    
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'image', 'category','is_active']    
    

        
admin.site.register(models.Category, CategoryAdmin)        
admin.site.register(models.SubCategory, SubCategoryAdmin)
