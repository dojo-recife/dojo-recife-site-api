from rest_framework import serializers
from .models import Participante
from django.utils import timezone


class ParticipanteSerializer(serializers.ModelSerializer):
    def validate_evento(self, value):
        if value.data_hora_limite < timezone.now():
            raise serializers.ValidationError('Passou do horário de inscrição do evento')

        return value

    class Meta:
        model = Participante
        fields = ("id", "nome", "email", "telefone", "documento", "evento")
        read_only = ("id",)
