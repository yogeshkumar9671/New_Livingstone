from django.apps import AppConfig

class LivingstoneAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'livingstone_app'

    def ready(self):
        import livingstone_app.signals 
