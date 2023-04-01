from rest_framework import viewsets, permissions
from .models import Participantes
from .serializers import ParticipantesSerializer


class ParticipantesViewSet(viewsets.ModelViewSet):
    queryset = Participantes.objects.all()
    serializer_class = ParticipantesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
