from rest_framework.routers import DefaultRouter
from .views import ParticipantesViewSet


router = DefaultRouter()
router.register("", ParticipantesViewSet)

urlpatterns = router.urls
