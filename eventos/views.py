from rest_framework import viewsets, permissions
from .models import Eventos
from .serializers import EventosSerializer


class EventosViewSet(viewsets.ModelViewSet):
    queryset = Eventos.objects.all()
    serializer_class = EventosSerializer
    permission_classes = [permissions.IsAuthenticated]
