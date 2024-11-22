from django.contrib import admin

from app.app_admin.models import Chat, Msg

admin.site.register(Chat)
admin.site.register(Msg)
