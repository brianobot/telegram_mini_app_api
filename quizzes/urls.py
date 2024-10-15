from rest_framework.routers import DefaultRouter

from quizzes import views

app_name = "quizzes"

router = DefaultRouter()
router.register("", views.QuestionViewSet, basename="question")


urlpatterns = router.urls