from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

from django.conf import settings
from django.conf.urls.static import static

from debug_toolbar.toolbar import debug_toolbar_urls

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
] + [
    *static(settings.STATIC_URL, document_root=settings.STATIC_ROOT),
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
] + debug_toolbar_urls()

