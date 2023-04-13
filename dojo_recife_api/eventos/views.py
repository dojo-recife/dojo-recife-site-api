from rest_framework import permissions, viewsets
from rest_framework.response import Response

from .models import Evento
from .serializers import EventoSerializer


class EventoViewSet(viewsets.ModelViewSet):
    serializer_class = EventoSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Evento.objects.all()
