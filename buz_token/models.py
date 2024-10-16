from django.db import models
from django.db.models import Sum

from config.model_utils import BaseModelMixin


class BuzToken(BaseModelMixin):
    CHANNEL_OPTIONS = (
        ("games", "games"),
        ("events", "events"),
        ("referrals", "referrals"),
    )
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    channel = models.CharField(max_length=20, choices=CHANNEL_OPTIONS)
    metadata = models.JSONField(default=dict, blank=True)
    """
        code: \"""
        
            \"""
    """


class Task(BaseModelMixin):
    description = models.TextField()
    max_users = models.IntegerField()
    reward = models.IntegerField()
    metadata = models.JSONField(default=dict, blank=True)

    def __str__(self) -> str:
        return f"{self.description} - {self.reward} BUZ"

    def can_reward_user(self) -> bool:
        return self.user_tasks.count() < self.max_users

    def reward_user(self, user) -> bool:
        if self.can_reward_user():
            try:
                UserTask.objects.create(user=user, task=self)
            except Exception:
                return False
            return True
        return False
    
    def evaluate_logic(self, user) -> bool:
        code_str = self.metadata.get("code", "def return_false(user): return False")
        print(f"✅✅✅ {code_str = }")
        exec(code_str)
        try:
            result = locals().get('func')(user)
            print(f"✅✅✅ {result = }")
        except Exception as err:
            print(f"❌❌❌ {err = }")
            return False
        return result

    @property
    def user_rewarded(self) -> int:
        return self.user_tasks.count()
    
    @property
    def tokens_awarded(self) -> int:
        return self.user_tasks.filter(task__id=self.id).aggregate(total=Sum('task__reward')).get('total', 0)


class UserTask(BaseModelMixin):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="user_tasks")
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="user_tasks")

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'task'], name='unique_user_task')
        ]

    @property
    def reward(self) -> int:
        return self.task.reward