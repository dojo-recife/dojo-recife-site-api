from rest_framework import serializers

from dojo_recife_api.participantes.serializers import ParticipanteSerializer

from .models import Evento


class EventoSerializer(serializers.ModelSerializer):
    participantes = ParticipanteSerializer(many=True, read_only=True)

    class Meta:
        model = Evento
        fields = ("id", "local", "data", "hora", "max_pessoas",
                  "data_hora_limite", "participantes")
        read_only_fields = ("id",)
