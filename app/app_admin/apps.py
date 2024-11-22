from django.apps import AppConfig


class AppAdminConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app.app_admin'

    def models(self):
      from app.app_admin.models import Chat
      from app.app_admin.models import Msg