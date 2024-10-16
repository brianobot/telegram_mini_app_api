from rest_framework.routers import DefaultRouter

from buz_token import views

app_name = "buz_token"

router = DefaultRouter()
router.register("tasks", views.TaskViewSet)


urlpatterns = router.urls