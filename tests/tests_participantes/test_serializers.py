import pytest
from dojo_recife_api.participantes.serializers import ParticipanteSerializer

pytestmark = pytest.mark.django_db


def test_create_participante_serializer(evento):
    evento.save()
    participante_data = {
        "nome": "Matheus",
        "email": "matheus@email.com",
        "telefone": "81999999999",
        "documento": "11111111111",
        "evento": evento.id,
    }
    serializer = ParticipanteSerializer(data=participante_data)
    serializer.is_valid(raise_exception=True)
    validated_data = serializer.validated_data
    participante = serializer.create(validated_data)

    assert participante.id


def test_create_evento_without_field_data(participante_payload):
    participante_payload.pop("nome")
    serializer = ParticipanteSerializer(data=participante_payload)
    assert not serializer.is_valid()


def test_create_partiicpante_with_field_blank(participante_payload):
    participante_payload["nome"] = ""
    serializer = ParticipanteSerializer(data=participante_payload)
    assert not serializer.is_valid()


def test_partial_update_participante_serializer(participante, evento):
    evento.save()
    old_name = participante.nome
    serializer = ParticipanteSerializer(instance=participante, data={"nome": "Novo Nome"}, partial=True)
    serializer.is_valid(raise_exception=True)
    updated_participante = serializer.save()

    assert updated_participante.id == participante.id
    assert updated_participante.nome != old_name
