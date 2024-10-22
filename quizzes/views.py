import random

from django.core.cache import cache
from django.utils import timezone

from rest_framework import viewsets
from rest_framework import serializers
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.request import Request

from quizzes.models import Question
from quizzes.models import UserQuestion
from quizzes.serializers import QuestionSerializer
from quizzes.serializers import AnsweredQuestionSerializer

from drf_spectacular.utils import extend_schema

from config.views import BaseView
from config.utils import seconds_until_next_day


class QuestionViewSet(BaseView, viewsets.ViewSet):
    serializer_class = QuestionSerializer

    def get_user_daily_question_reward(self, request: Request) -> int:
        user_question_count = UserQuestion.objects.filter(user=request.user, created_at__date=timezone.now().date()).count()
        return user_question_count * 700

    def get_user_daily_question_count(self, request: Request) -> int:
        user_id = request.user.id
        return cache.get(f"{user_id}_daily_question_count", 0)

    def set_user_daily_question_count(self, request: Request) -> int:
        user_id = request.user.id
        current_daily_question_count = self.get_user_daily_question_count(request)
        updated_daily_question_count = current_daily_question_count + 1
        cache.set(f"{user_id}_daily_question_count", updated_daily_question_count, timeout=seconds_until_next_day())
        return updated_daily_question_count

    def set_user_tried_daily_question(self, request: Request, question_id: str) -> int:
        user_id = request.user.id
        question_ids = cache.get(f"{user_id}_tried_question_ids", [])
        question_ids.append(question_id)
        cache.set(f"{user_id}_tried_question_ids", question_ids, timeout=seconds_until_next_day())
        return True

    @extend_schema(
        operation_id="question_get",
    )
    @action(detail=False, methods=['GET'])
    def question(self, request, *args, **kwargs):
        """
        This endpoint returns a random question from the db for the particular user
        """
        question_count = self.get_user_daily_question_count(request)
        if question_count >= 7:
            msg = "Maximum Daily Question Reached"
            raise serializers.ValidationError({"detail": msg})

        user_answered_questions_ids = UserQuestion.objects.filter(user=request.user).values_list('question_id', flat=True)

        # Exclude these questions from the available pool
        tried_question_ids = cache.get(f"{request.user.id}_tried_question_ids", [])
        remaining_questions = Question.objects.exclude(id__in=[
            *user_answered_questions_ids,
            *tried_question_ids,
        ])
        
        if remaining_questions.exists():
            # Get a random question from the remaining pool
            random_question = remaining_questions[random.randint(0, remaining_questions.count() - 1)]
            serializer = self.serializer_class(random_question)
            question_count = self.set_user_daily_question_count(request)
            self.set_user_tried_daily_question(request, random_question.id)
            todays_reward = self.get_user_daily_question_reward(request)
            return Response({
                    "daily_question_count": question_count, 
                    "daily_question_reward": todays_reward,
                    **serializer.data
                })
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
    def answered(self, request: Request, *args, **kwargs):
        """
        This endpoints marked a particular question specified by it's id as answered by the user
        """
        serializer = AnsweredQuestionSerializer(data=request.data, context=self.get_renderer_context())
        serializer.is_valid(raise_exception=True)
        question = serializer.validated_data.get("question")
        today = timezone.now().date()
        user_today_question_count = UserQuestion.objects.filter(created_at__date=today).count()
        if user_today_question_count >= 7:
            msg = "Daily Question Count exceeded!"
            raise serializers.ValidationError({"detail": msg})
        
        UserQuestion.objects.create(user=request.user, question=question)
        return Response(data={"detail": "ok"})

