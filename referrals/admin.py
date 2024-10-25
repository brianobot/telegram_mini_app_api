from django.contrib import admin

from referrals.models import Referral


@admin.register(Referral)
class ReferralAdmin(admin.ModelAdmin):
    list_display = ['referred', 'referred_fullname', 'referrer', 'referrer_fullname', 'created_at']