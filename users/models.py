from django.db import models


class User(models.Model):
    id = models.CharField(
        primary_key=True, blank=False, editable=True, max_length=255
    )
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False, db_index=True)

    def __str__(self) -> str:
        return f"User(id={self.id})"
    
    @property
    def referrals(self) -> int:
        return self.referals.count()
    
    @property
    def buz_tokens(self) -> int:
        return 1000