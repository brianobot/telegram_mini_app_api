from django.contrib import admin
from django.db.models.query import QuerySet
from django.http import HttpRequest

from quizzes.models import UserQuestion
from quizzes.models import Question
from quizzes.models import Option


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['text', 'answer', 'created_at', 'updated_at']


@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    list_display = ['text', 'created_at', 'updated_at']


@admin.register(UserQuestion)
class UserQuestionAdmin(admin.ModelAdmin):
    list_display = ['user', 'question', 'created_at', 'updated_at']

    def get_queryset(self, request: HttpRequest) -> QuerySet:
        return super().get_queryset(request).select_related('user')
    