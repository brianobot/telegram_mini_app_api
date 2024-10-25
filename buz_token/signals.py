from django.db.models.signals import post_save
from django.dispatch import receiver

from buz_token.models import BuzToken
from buz_token.models import UserTask


@receiver(post_save, sender=UserTask)
def reward_buz_token(sender, instance: UserTask, created, *args, **kwargs):
    if created:
        reward = instance.task.reward
        BuzToken.objects.create(
            amount=reward, 
            channel="events",
            user=instance.user, 
            metadata={"task_id": instance.task.id},
        )
