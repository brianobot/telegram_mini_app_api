from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("users.urls")),
    path("api/", include("quizzes.urls")),
    path("api/", include("referrals.urls")),
    path("api/", include("buz_token.urls")),
]
