from django.contrib import admin
from .models import User

class AccountsAdmin(admin.ModelAdmin):
    list_display = ('username','email','phone',)

admin.site.register(User,AccountsAdmin)