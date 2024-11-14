from django.contrib import admin

from users.models import User


@admin.register(User)
class BuzzUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'referrals', 'fullname', 'buz_tokens', 'created_at', 'updated_at']
    search_fields = ['id']
    actions = ['set_default_profile_pic']

    @admin.action(description="Set Default profile image if it null")
    def set_default_profile_pic(self, request, queryset):
        default_profile_image = "profile_images/default_image.jpg"
        for user in queryset:
            user: User
            if not user.profile_image:
                user.profile_image = default_profile_image
                user.save()
