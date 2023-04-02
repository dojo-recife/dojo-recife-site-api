from rest_framework import serializers
from .models import Evento


class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = ("id", "local", "data", "hora", "max_pessoas", "data_hora_limite")
        read_only_fields = ("id",)
