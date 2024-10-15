import random

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from quizzes.models import Question
from quizzes.serializers import QuestionSerializer
from quizzes.serializers import AnsweredQuestionSerializer

from config.views import BaseView


class QuestionViewSet(BaseView, viewsets.ViewSet):
    serializer_class = QuestionSerializer

    @action(detail=False, methods=['GET'])
    def question(self, request, *args, **kwargs):
        """
        This endpoint returns a random question from the db for the particular user
        """
        user = self.get_user()
        random_question = Question.objects.all()[random.randint(0, Question.objects.count() - 1)]
        serializer = self.serializer_class(random_question)
        return Response(serializer.data)
    
    @action(detail=False, methods=['GET'], url_path="question/(?P<question_id>[^/.]+)")
    def get_question(self, request, *args, **kwargs):
        """
        This endpoint returns a specific question by id from the db.
        """
        question = Question.objects.filter(id=kwargs.get("question_id")).first()
        serializer = self.serializer_class(question)
        return Response(serializer.data)
    
    @action(detail=False, methods=['POST'])
    def answered(self, request, *args, **kwargs):
        serializer = AnsweredQuestionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data)

