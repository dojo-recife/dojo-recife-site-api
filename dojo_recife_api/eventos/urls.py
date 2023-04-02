from rest_framework.routers import DefaultRouter
from .views import EventoViewSet


router = DefaultRouter()
router.register("", EventoViewSet)

urlpatterns = router.urls
