from django.apps import AppConfig


class Mediacategory_templateConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mediacategory_template'
    
    def ready(self):
        import mediacategory_api.signals