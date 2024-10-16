from django.db import models
from django.db.models import Sum

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

from users.managers import UserManager



class User(AbstractBaseUser, PermissionsMixin):
    id = models.CharField(
        primary_key=True, blank=False, editable=True, max_length=255
    )
    # Permissions fields
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    # timestamp fields
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False, db_index=True)

    USERNAME_FIELD = 'id'

    objects = UserManager()

    def __str__(self) -> str:
        return f"User(id={self.id})"
    
    @property
    def referrals(self) -> int:
        return self.referals.count()
    
    @property
    def buz_tokens(self) -> int:
        return self.buztoken_set.aggregate(total=Sum('amount')).get('total', 0)