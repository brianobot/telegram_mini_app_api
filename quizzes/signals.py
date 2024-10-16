from django.db.models.signals import post_save
from django.dispatch import receiver

from quizzes.models import UserQuestion
from buz_token.models import BuzToken


@receiver(post_save, sender=UserQuestion)
def reward_buz_token(sender, instance: UserQuestion, created, *args, **kwargs):
    if created:
        reward = 700
        BuzToken.objects.create(
            amount=reward, 
            channel="games",
            user=instance.user, 
        )
