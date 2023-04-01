from rest_framework import serializers
from .models import Eventos
from rest_flex_fields import FlexFieldsModelSerializer


class EventosSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Eventos
        fields = "__all__"
