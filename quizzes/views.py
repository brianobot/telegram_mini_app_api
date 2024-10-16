import random

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from quizzes.models import Question
from quizzes.models import UserQuestion
from quizzes.serializers import QuestionSerializer
from quizzes.serializers import AnsweredQuestionSerializer

from drf_spectacular.utils import extend_schema

from config.views import BaseView


class QuestionViewSet(BaseView, viewsets.ViewSet):
    serializer_class = QuestionSerializer

    @extend_schema(
        operation_id="question_get",
    )
    @action(detail=False, methods=['GET'])
    def question(self, request, *args, **kwargs):
        """
        This endpoint returns a random question from the db for the particular user
        """
        user_answered_questions_ids = UserQuestion.objects.filter(user=request.user).values_list('question_id', flat=True)

        # Exclude these questions from the available pool
        remaining_questions = Question.objects.exclude(id__in=user_answered_questions_ids)
        
        if remaining_questions.exists():
            # Get a random question from the remaining pool
            random_question = remaining_questions[random.randint(0, remaining_questions.count() - 1)]
            serializer = self.serializer_class(random_question)
            return Response(serializer.data)
        else:
            return Response({"detail": "No more questions available for the user."}, status=404)
    
    @extend_schema(
        operation_id="question_retrieve",
    )
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
        """
        This endpoints marked a particular question specified by it's id as answered by the user
        """
        serializer = AnsweredQuestionSerializer(data=request.data, context=self.get_renderer_context())
        serializer.is_valid(raise_exception=True)
        return Response(data={"detail": "ok"})

