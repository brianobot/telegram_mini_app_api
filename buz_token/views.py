from rest_framework import status
from rest_framework import viewsets
from rest_framework import serializers
from rest_framework.decorators import action
from rest_framework.response import Response

from buz_token.serializers import TaskSerializer
from buz_token.models import UserTask
from buz_token.models import Task


class TaskViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all().reverse()

    @action(detail=True)
    def claim(self, request, *args, **kwargs):
        task = self.get_object()
        user = request.user
        if not task.can_reward_user():
            msg = "task is no longer available"
            raise serializers.ValidationError({"detail": msg})

        if UserTask.objects.filter(task=task, user=user).exists():
            msg = "task already completed"
            raise serializers.ValidationError({"detail": msg})
        
        if not task.evaluate_logic(user):
            msg = "task not completed"
            raise serializers.ValidationError({"detail": msg})
        
        task.reward_user(user)
        return Response({"detail": "Task completed sucessfully"}, status=status.HTTP_202_ACCEPTED)