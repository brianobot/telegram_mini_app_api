from django.db import models
from django.db.models import Sum
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

from users.managers import UserManager



class User(AbstractBaseUser, PermissionsMixin):
    id = models.CharField(
        primary_key=True, blank=False, editable=True, max_length=255
    )
    metadata = models.JSONField(default=dict, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
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
        return self.buztoken_set.aggregate(total=Sum('amount')).get('total', 0) or 0
    
    @property
    def buz_token_distro(self) -> dict:
        return {
            "games": self.buztoken_set.filter(channel="games").aggregate(total=Sum('amount')).get('total', 0) or 0,
            "events": self.buztoken_set.filter(channel="events").aggregate(total=Sum('amount')).get('total', 0) or 0,
            "referrals": self.buztoken_set.filter(channel="referrals").aggregate(total=Sum('amount')).get('total', 0) or 0,
        }
    
    @property
    def position(self) -> int:
        leaders = User.objects.annotate(
            total_buztokens=Sum('buztoken__amount'),
        ).order_by('-total_buztokens').values('id')
        leaders_list = [leader.get('id') for leader in leaders]
        return leaders_list.index(self.id) + 1
    
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
    def fullname(self) -> str:
        default_first_name = self.id or self.first_name
        default_last_name = self.last_name or ' ' 
        return f"{default_first_name} {default_last_name}".strip()
    
    @property
    def language_code(self) -> str:
        return self.metadata.get("language_code")