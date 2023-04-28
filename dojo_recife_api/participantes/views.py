from rest_framework import permissions, viewsets

from .models import Participante
from .serializers import ParticipanteSerializer


class ParticipanteViewSet(viewsets.ModelViewSet):
    serializer_class = ParticipanteSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        queryset = Participante.objects.all()
        evento = self.request.query_params.get('evento')
        if evento:
            queryset = queryset.filter(evento=evento)
        return queryset
