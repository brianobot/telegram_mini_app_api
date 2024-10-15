from django.db import models

from config.model_utils import BaseModelMixin


class Question(BaseModelMixin):
    text = models.CharField(max_length=255)

    @property
    def answer(self) -> str:
        option = self.options.filter(is_correct=True).first()
        return getattr(option, "text", None)


class Option(BaseModelMixin):
    text = models.CharField(max_length=255)
    question = models.ForeignKey("quizzes.Question", on_delete=models.CASCADE, related_name="options")
    is_correct = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"Option(text={self.text})"


class UserQuestion(BaseModelMixin):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="user_questions")
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="user_questions")

