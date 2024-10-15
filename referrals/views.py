from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


from referrals.serializers import ReferralSerializer

class ReferralViewSet(viewsets.ViewSet):
    serializer_class = ReferralSerializer

    @action(detail=False, methods=['POST'])
    def refer(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.validated_data)