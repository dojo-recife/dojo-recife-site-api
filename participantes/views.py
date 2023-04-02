from rest_framework import viewsets, permissions
from .models import Participante
from .serializers import ParticipanteSerializer


class ParticipanteViewSet(viewsets.ModelViewSet):
    queryset = Participante.objects.select_related().all()
    serializer_class = ParticipanteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
