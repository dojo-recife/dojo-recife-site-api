from rest_framework.routers import DefaultRouter
from .views import EventosViewSet


router = DefaultRouter()
router.register("", EventosViewSet)

urlpatterns = router.urls
