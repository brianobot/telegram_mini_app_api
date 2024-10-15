from rest_framework import serializers

from quizzes.models import Question
from quizzes.models import Option


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ["text"]


class QuestionSerializer(serializers.ModelSerializer):
    question = serializers.CharField(source='text')
    options = serializers.SerializerMethodField()
    
    class Meta:
        model = Question
        fields = [
            "id",
            "question",
            "options",
            "answer",
            "created_at",
            "updated_at",
        ]

    def get_options(self, instance: Question) -> list[str]:
        return [option.text for option in instance.options.all()]
    

class AnsweredQuestionSerializer(serializers.Serializer):
    question: str = serializers.PrimaryKeyRelatedField(queryset=Question.objects.all())