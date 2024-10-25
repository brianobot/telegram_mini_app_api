from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    position = serializers.SerializerMethodField()
    referral_link = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
            "fullname",
            "language_code",
            "position",
            "referrals",
            "buz_tokens",
            "referral_link",
            "buz_token_distro",
            "created_at",
            "updated_at",
        ]

    def get_position(self, instance: User) -> int | None:
        return getattr(instance, "position", None)

    def get_referral_link(self, instance: User) -> str:
        user_id = getattr(instance, "id", None)
        return f"https://t.me/obot_test_bot?start={user_id}"


class UpdateUserMetadataSerializer(serializers.Serializer):
    id = serializers.CharField(allow_null=True, required=False)
    is_bot = serializers.BooleanField(allow_null=True, required=False)
    first_name = serializers.CharField(allow_null=True, required=False)
    last_name = serializers.CharField(allow_null=True, required=False)
    username = serializers.CharField(allow_null=True, required=False)
    language_code = serializers.CharField(allow_null=True, required=False)
    can_join_groups = serializers.BooleanField(allow_null=True, required=False)
    can_read_all_group_messages = serializers.BooleanField(allow_null=True, required=False)
    supports_inline_queries = serializers.BooleanField(allow_null=True, required=False)
    is_premium = serializers.BooleanField(allow_null=True, required=False)
    added_to_attachment_menu = serializers.BooleanField(allow_null=True, required=False)