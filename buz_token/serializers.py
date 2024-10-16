from rest_framework import serializers

from buz_token.models import Task
from buz_token.models import UserTask


class TaskSerializer(serializers.ModelSerializer):
    completed = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = [
            "id",
            "reward",
            "max_users",
            "description",
            "completed",
            "created_at",
            "updated_at",
        ]

    def get_completed(self, instance: Task) -> bool:
        return UserTask.objects.filter(task=instance).exists()