from django.contrib import admin
from apps.base.models import Settings, Projects, Directors
# Register your models here.

@admin.register(Settings)
class BaseAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'logo', 'email', 'contact', 'address', 'instagram', 'whatsapp', 'facebook', 'youtube']

@admin.register(Projects)
class BaseAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'urls']

@admin.register(Directors)
class BaseAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'description']