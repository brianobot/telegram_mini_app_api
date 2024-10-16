from django.contrib import admin

from users.models import User


@admin.register(User)
class BuzzUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'referrals', 'buz_tokens', 'created_at', 'updated_at']