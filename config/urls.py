from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse


from rest_framework.views import APIView
from rest_framework.response import Response

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)


def root(request):
    return JsonResponse({"detail": "ok"})


urlpatterns = [
    path("", root),
    path("admin/", admin.site.urls),
    path("api/", include("users.urls")),
    path("api/", include("quizzes.urls")),
    path("api/", include("referrals.urls")),
    path("api/", include("buz_token.urls")),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),  # JSON Schema generation
    path("api/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),  # Redoc UI
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema"),name="swagger-ui",),  # Swagger UI
]
