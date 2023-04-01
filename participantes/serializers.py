from rest_framework import serializers
from .models import Participantes
from eventos.serializers import EventosSerializer


class ParticipantesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participantes
        fields = "__all__"
        expandable_fields = {"evento": EventosSerializer}