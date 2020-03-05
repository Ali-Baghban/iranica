from django.contrib import admin
from .models import *

@admin.register(Settings)

class SettingsAdmin(admin.ModelAdmin):
    list_display = ('site_title', 'status','email',)
    list_editable = ('status',)

@admin.register(Rules)

class RulesAdmin(admin.ModelAdmin):
    list_display = ('title',)
    