from django.db import models
from django.db.models import Q, F

from config.model_utils import BaseModelMixin


class Referral(BaseModelMixin):
    referred = models.OneToOneField('users.User', on_delete=models.CASCADE, related_name="referral")
    referrer = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name="referals")

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=~Q(referred_id=F('referrer_id')),
                name='check_referred_not_referer'
            )
        ]
        indexes = [
            models.Index(fields=['referrer']),
        ]
