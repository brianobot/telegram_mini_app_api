from rest_framework import serializers

from  referrals.models import Referral


class ReferralSerializer(serializers.ModelSerializer):
    class Meta:
        model = Referral
        fields = [
            "id",
            "referred",
            "referrer",
            "created_at",
            "updated_at",
        ]

    def create(self, validated_data: dict) -> Referral:
        try:
            referral = super().create(validated_data)
        except Exception as err:
            raise serializers.ValidationError(str(err))
        return referral