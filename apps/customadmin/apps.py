from django.apps import AppConfig

class CustomadminConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'customadmin'
    
    def ready(self):
        import mediacategory_api.signals