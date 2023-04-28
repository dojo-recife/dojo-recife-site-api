from rest_framework.routers import DefaultRouter

from .views import ParticipanteViewSet

router = DefaultRouter()
router.register("", ParticipanteViewSet, basename='participantes')

urlpatterns = router.urls
