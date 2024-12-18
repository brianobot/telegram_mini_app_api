from rest_framework import serializers

from buz_token.models import Task
from buz_token.models import UserTask


class TaskSerializer(serializers.ModelSerializer):
    completed = serializers.SerializerMethodField()
    is_available = serializers.BooleanField(source="can_reward_user")

    class Meta:
        model = Task
        fields = [
            "id",
            "reward",
            "action",
            "max_users",
            "description",
            "completed",
            "is_available",
            "created_at",
            "updated_at",
        ]

    def get_completed(self, instance: Task) -> bool:
        user = self.context.get("request").user
        return UserTask.objects.filter(user=user, task=instance).exists()