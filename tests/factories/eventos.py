from unittest import mock
import factory
from dojo_recife_api.eventos.models import Evento


class EventoFactory(factory.Factory):
    local = "UFPE - Cin"
    data = "2023-03-13"
    hora = "19:00:00"
    max_pessoas = 30
    data_hora_limite = "2023-03-13T12:00:00Z"

    class Meta:
        model = Evento
