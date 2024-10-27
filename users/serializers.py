from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "position",
            "referrals",
            "fullname",
            "profile_image",
            "buz_tokens",
            "buz_token_distro",
            "referral_link",
            "created_at",
            "updated_at",
        ]


class LeaderBoardUserSerializer(serializers.ModelSerializer):
    position = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            "id",
            "fullname",
            "profile_image",
            "position",
            "buz_tokens",
            "created_at",
            "updated_at",
        ]
    
    def get_position(self, instance: User) -> int | None:
        return getattr(instance, "position", None)


class UpdateUserMetadataSerializer(serializers.Serializer):
    id = serializers.CharField(allow_null=True, required=False)
    is_bot = serializers.BooleanField(allow_null=True, required=False)
    first_name = serializers.CharField(allow_null=True, required=False)
    last_name = serializers.CharField(allow_null=True, required=False)
    username = serializers.CharField(allow_null=True, required=False)
    language_code = serializers.CharField(allow_null=True, required=False)
    profile_image = serializers.ImageField(allow_null=True, required=False)
    can_join_groups = serializers.BooleanField(allow_null=True, required=False)
    can_read_all_group_messages = serializers.BooleanField(allow_null=True, required=False)
    supports_inline_queries = serializers.BooleanField(allow_null=True, required=False)
    is_premium = serializers.BooleanField(allow_null=True, required=False)
    added_to_attachment_menu = serializers.BooleanField(allow_null=True, required=False)