from django.contrib import admin
from .models import MediaCategory, MediaImage, MediaVideo

class MediaCategoryAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ["pk", "category"]

class MediaImageAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ["pk", "category", "image"]

class MediaVideoAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ["pk", "category", "video"]

admin.site.register(MediaCategory, MediaCategoryAdmin)
admin.site.register(MediaImage, MediaImageAdmin)
admin.site.register(MediaVideo, MediaVideoAdmin)