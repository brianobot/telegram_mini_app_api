from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    referral_link = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            "id",
            "referrals",
            "buz_tokens",
            "referral_link",
            "buz_token_distro",
            "created_at",
            "updated_at",
        ]
    
    def get_referral_link(self, instance: User) -> str:
        return f"https://t.me/obot_test_bot?start={instance.id}"
