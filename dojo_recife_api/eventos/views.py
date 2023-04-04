from rest_framework import permissions, viewsets
from rest_framework.response import Response

from .models import Evento
from .serializers import EventoSerializer, ParticipanteSerializer


class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer
    permission_classes = [permissions.IsAuthenticated]


class EventoParticipanteViewSet(viewsets.ModelViewSet):
    """
    Exibe todos os eventos e seus participantes inscritos.
    """
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer

    def retrieve(self):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        # incluir os participantes inscritos em cada evento
        participantes = ParticipanteSerializer(instance.participantes.all(),
                                               many=True).data
        data = serializer.data
        data['participantes'] = participantes

        return Response(data)
