from datetime import date, datetime, time
import pytest


@pytest.fixture
def evento_payload(evento):
    return {
        "local": evento.local,
        "data": evento.data,
        "hora": evento.hora,
        "max_pessoas": evento.max_pessoas,
        "data_hora_limite": evento.data_hora_limite,
    }
