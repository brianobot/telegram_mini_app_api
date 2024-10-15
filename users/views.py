from rest_framework import views, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from users.serializers import UserSerializer
from users.models import User


class UserViewSet(viewsets.ViewSet):
    serializer_class = UserSerializer

    @action(detail=False, methods=['POST'])
    def users(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.get_or_create()
        serializer = self.serializer_class(user)
        return Response(serializer.data)
    
    @action(detail=False, methods=['GET'])
    def leaderboard(self, request, *args, **kwargs):
        leaders = User.objects.all()
        serializer = self.serializer_class(leaders, many=True)
        return Response(serializer.data)
    
