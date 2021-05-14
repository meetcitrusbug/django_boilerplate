from django.contrib import admin
from rest_framework.authtoken.models import Token
from . import models

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'product_number', 'sub_category','product_shipping_method', 'status', 'price', 'is_active']
    
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'image']
    
class ProductTagAdmin(admin.ModelAdmin):
    list_display = ['id', 'tag', 'product']

admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.ProductImage, ProductImageAdmin)
admin.site.register(models.ProductTag, ProductTagAdmin)