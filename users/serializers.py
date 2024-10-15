from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    id = serializers.CharField()
    
    class Meta:
        model = User
        fields = [
            "id",
            "buz_tokens",
            "referrals",
            "created_at",
            "updated_at",
        ]

    def get_or_create(self):
        user_id = self.validated_data.get("id")
        user, created = User.objects.get_or_create(id=user_id)
        return user