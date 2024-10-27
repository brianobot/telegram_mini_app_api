from django.db import models 
from django.db.models import Sum
from django.db.models import Window
from django.db.models.functions import Coalesce
from django.db.models.functions import RowNumber

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.request import Request

from users.serializers import UserSerializer
from users.serializers import LeaderBoardUserSerializer
from users.serializers import UpdateUserMetadataSerializer
from users.models import User


class UserViewSet(viewsets.ViewSet):
    serializer_class = UserSerializer

    @action(detail=False, methods=['GET', 'OPTIONS', 'HEAD', 'TRACE'])
    def users(self, request: Request, *args, **kwargs):
        serializer = self.serializer_class(request.user, context=self.get_renderer_context())
        return Response(serializer.data)
       
    @action(detail=False, methods=['POST', 'OPTIONS', 'HEAD', 'TRACE'], serializer_class=UpdateUserMetadataSerializer)
    def update_user(self, request: Request, *args, **kwargs):
        user: User = self.request.user
        serializer = self.serializer_class(data=request.data, context=self.get_renderer_context())
        serializer.is_valid(raise_exception=True)
        user.profile_image = serializer.validated_data.pop("profile_image", None)
        user.metadata.update(**serializer.validated_data)
        user.save()
        serializer = UserSerializer(user, context=self.get_renderer_context())
        return Response(serializer.data)

    @action(detail=False, methods=['GET', 'OPTIONS', 'HEAD', 'TRACE'], serializer_class=LeaderBoardUserSerializer)
    def leaderboard(self, request, *args, **kwargs):
        leaders = User.objects.annotate(
            total_buztokens=Coalesce(Sum('buztoken__amount'), 0),
            position=Window(
                expression=RowNumber(),
                order_by=models.F('total_buztokens').desc()
            )
        ).order_by('-total_buztokens', "created_at")
        serializer = self.serializer_class(leaders, many=True, context=self.get_renderer_context())
        return Response(serializer.data)
    
