from rest_framework import views, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.request import Request

from users.serializers import UserSerializer
from users.models import User


class UserViewSet(viewsets.ViewSet):
    serializer_class = UserSerializer

    @action(detail=False, methods=['GET'])
    def users(self, request: Request, *args, **kwargs):
        serializer = self.serializer_class(request.user)
        return Response(serializer.data)
       
    @action(detail=False, methods=['GET'])
    def leaderboard(self, request, *args, **kwargs):
        leaders = User.objects.all()
        serializer = self.serializer_class(leaders, many=True)
        return Response(serializer.data)
    
