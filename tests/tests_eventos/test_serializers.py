import pytest
from dojo_recife_api.eventos.serializers import EventoSerializer

pytestmark = pytest.mark.django_db


def test_create_evento_serializer_data(evento):
    serializer = EventoSerializer(instance=evento)
    assert serializer.data == {
        "id": str(evento.id),
        "local": evento.local,
        "data": evento.data,
        "hora": evento.hora,
        "max_pessoas": evento.max_pessoas,
        "data_hora_limite": evento.data_hora_limite,
    }


def test_create_evento_serializer(evento_payload):
    serializer = EventoSerializer(data=evento_payload)
    serializer.is_valid(raise_exception=True)
    validated_data = serializer.validated_data
    evento = serializer.create(validated_data)

    assert evento.id


def test_create_evento_without_field_data(evento_payload):
    evento_payload.pop("local")
    serializer = EventoSerializer(data=evento_payload)
    assert not serializer.is_valid()


def test_create_evento_with_field_blank(evento_payload):
    evento_payload["local"] = ""
    serializer = EventoSerializer(data=evento_payload)
    assert not serializer.is_valid()


def test_partial_update_evento_serializer(evento):
    old_local = evento.local
    serializer = EventoSerializer(instance=evento, data={"local": "Novo Local"}, partial=True)
    serializer.is_valid(raise_exception=True)
    updated_evento = serializer.save()

    assert updated_evento.id == evento.id
    assert updated_evento.local != old_local
