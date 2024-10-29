from django.db import models
from django.db.models import Sum
from django.db.models.functions import Coalesce
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

from users.managers import UserManager



class User(AbstractBaseUser, PermissionsMixin):
    id = models.CharField(
        primary_key=True, blank=False, editable=True, max_length=255
    )
    profile_image = models.ImageField(blank=True, null=True, upload_to="profile_images", default="default_image.jpg")
    metadata = models.JSONField(default=dict, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False, db_index=True)

    USERNAME_FIELD = 'id'

    objects = UserManager()

    def __str__(self) -> str:
        return f"User({self.fullname})"
    
    @property
    def referrals(self) -> int:
        return self.referals.count()
    
    @property
    def buz_tokens(self) -> int:
        return self.buztoken_set.aggregate(Sum('amount'))['amount__sum'] or 0
    
    @property
    def buz_token_distro(self) -> dict:
        distribution = (
            self.buztoken_set
            .values("channel")
            .annotate(total=Sum("amount"))
        )
        result = {"games": 0, "events": 0, "referrals": 0}
        for entry in distribution:
            result[entry["channel"]] = entry.get("total", 0)
        
        return result
    
    @property
    def position(self) -> int:
        leaders = User.objects.annotate(
            total_buztokens=Coalesce(Sum('buztoken__amount'), 0),
        ).order_by('-total_buztokens', 'created_at').values_list('id', flat=True)
        return list(leaders).index(self.id) + 1
    
    @position.setter
    def position(self, value) -> int:
        return value
        
    @property
    def first_name(self) -> str | None:
        return self.metadata.get("first_name")
    
    @property
    def last_name(self) -> str | None:
        return self.metadata.get("last_name")
    
    @property
    def username(self) -> str:
        return self.metadata.get("username")

    @property
    def fullname(self) -> str:
        default_first_name = self.first_name or self.id 
        default_last_name = self.last_name or ' ' 
        return f"{default_first_name} {default_last_name}".strip()
    
    @property
    def referral_link(self) -> str:
        return f"https://t.me/buzmode_bot?start={self.id}"