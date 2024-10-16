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
    queryset = Task.objects.all()

    @action(detail=True)
    def claim(self, request, *args, **kwargs):
        task = self.get_object()
        if not task.can_reward_user():
            msg = "Task is no longer available"
            raise serializers.ValidationError({"detail": msg})

        if UserTask.objects.filter(task=task).exists():
            msg = "task already completed"
            raise serializers.ValidationError({"detail": msg})
        
        if not task.evaluate_logic(request.user):
            msg = "task not completed"
            raise serializers.ValidationError({"detail": msg})
        
        task.reward_user(request.user)
        return Response(status=status.HTTP_202_ACCEPTED)