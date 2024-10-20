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
            "buz_token_distro",
            "created_at",
            "updated_at",
        ]
