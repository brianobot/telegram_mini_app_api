from django.db.models.signals import post_save
from django.dispatch import receiver

from referrals.models import Referral
from buz_token.models import BuzToken


@receiver(post_save, sender=Referral)
def reward_buz_token(sender, instance: Referral, created, *args, **kwargs):
    if created:
        BuzToken.objects.create(
            user=instance.referrer,
            amount=42000,
            channel="referrals",
            metadata={},
        )
