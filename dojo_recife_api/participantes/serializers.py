from rest_framework import serializers
from .models import Participante
from django.utils import timezone


class ParticipanteSerializer(serializers.ModelSerializer):
    # Validar horário limite para inscrição do evento
    def validate_evento(self, value):
        limite_evento = value.data_hora_limite
        datatime_atual = timezone.now()

        if limite_evento < datatime_atual:
            raise serializers.ValidationError('Passou do horário de inscrição do evento ' + datatime_atual.strftime('%m %d %y %H %M'))
        return value

    class Meta:
        model = Participante
        fields = ("id", "nome", "email", "telefone", "documento", "evento")
        read_only = ("id",)
