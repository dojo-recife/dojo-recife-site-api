from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import EventoViewSet, EventoParticipanteViewSet

router = DefaultRouter()
router.register(r"evento", EventoViewSet)
router.register(r"eventos-participantes", EventoParticipanteViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
