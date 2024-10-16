from rest_framework import viewsets


class TaskViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = None
    queryset = None