from rest_framework.routers import DefaultRouter

from referrals import views

app_name = "referrals"

router = DefaultRouter()
router.register("", views.ReferralViewSet, basename="refer")


urlpatterns = router.urls