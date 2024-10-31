from django.contrib import admin
from django.http import JsonResponse
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

admin.site.site_header = "Buz-Mode Web App"
admin.site.site_title = "Buz-Mode Web App Admin site"
admin.site.index_title = "Buz-Mode Web App Admin"


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
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    from debug_toolbar.toolbar import debug_toolbar_urls

    urlpatterns += debug_toolbar_urls()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)