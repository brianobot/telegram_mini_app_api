from django.contrib import admin

from users.models import User


@admin.register(User)
class BuzzUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_at', 'updated_at']