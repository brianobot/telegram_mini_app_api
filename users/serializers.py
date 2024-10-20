from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):    
    class Meta:
        model = User
        fields = [
            "id",
            "referrals",
            "buz_tokens",
            "buz_token_distro",
            "created_at",
            "updated_at",
        ]
