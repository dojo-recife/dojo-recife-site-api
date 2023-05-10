import uuid
from http import HTTPStatus

import pytest
from pytest_factoryboy.fixture import register
from rest_framework.reverse import reverse

from tests.factories.eventos import EventoFactory
from tests.factories.participantes import Participante, ParticipanteFactory

pytestmark = pytest.mark.django_db

register(EventoFactory, "another_evento")
register(ParticipanteFactory, "another_participante")


def create_participante(participante_factory, evento, amount=1):
    evento.save()
    for _ in range(amount):
        participante_factory(evento=evento).save()


def test_list_participantes(client, participante_factory, evento):
    create_participante(participante_factory, evento, 2)
    url = reverse("participantes-list")
    response = client.get(url)
    assert response.status_code == HTTPStatus.OK
    assert len(response.json()) == 2


def test_create_participante(client, evento, participante_payload):
    evento.save()
    url = reverse("participantes-list")
    response = client.post(url, participante_payload)
    assert response.status_code == HTTPStatus.CREATED


@pytest.mark.parametrize(
    "field", ["nome", "email", "telefone", "documento"]
)
def test_create_participante_without_field(field, client, participante_payload, evento):
    evento.save()
    participante_payload.pop(field)
    url = reverse("participantes-list")
    response = client.post(url, participante_payload)
    assert response.status_code == HTTPStatus.BAD_REQUEST


@pytest.mark.parametrize(
    "field", ["nome", "email", "telefone", "documento"]
)
def test_create_evento_with_field_blank(field, client, participante_payload, evento):
    evento.save()
    participante_payload[field] = ""
    url = reverse("participantes-list")
    response = client.post(url, participante_payload)
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_detail_participante(client, participante, evento):
    evento.save()
    participante.save()
    url = reverse("participantes-detail", kwargs={"pk": participante.id})
    response = client.get(url)
    assert response.status_code == HTTPStatus.OK


def test_detail_participante_nonexistent(client):
    url = reverse("participantes-detail", kwargs={"pk": 123})
    response = client.get(url)
    assert response.status_code == HTTPStatus.NOT_FOUND


def test_update_participante(client, participante, evento):
    evento.save()
    participante.save()
    url = reverse("participantes-detail", kwargs={"pk": participante.id})
    payload = {
        "nome": "Ana",
        "email": "ana@email.com",
        "telefone": "81988888888",
        "documento": "22222222222",
        "evento": evento.id
    }
    response = client.put(url, payload, content_type="application/json")

    assert response.status_code == HTTPStatus.OK
    assert str(participante.id) == response.json()["id"]
    assert participante.nome != response.json()["nome"]
    assert participante.email != response.json()["email"]
    assert participante.telefone != response.json()["telefone"]
    assert participante.documento != response.json()["documento"]


def test_fail_update_participante(client, participante, evento):
    evento.save()
    participante.save()
    url = reverse("participantes-detail", kwargs={"pk": participante.id})
    payload = {
        "nome": "Teste",
    }
    response = client.put(url, payload, content_type="application/json")

    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_partial_update_participante(client, participante, evento):
    evento.save()
    participante.save()
    url = reverse("participantes-detail", kwargs={"pk": participante.id})
    payload = {"email": "newemail@email.com"}
    response = client.patch(url, payload, content_type="application/json")

    assert response.status_code == HTTPStatus.OK
    assert participante.email != response.json()["email"]


    #Testar a filtragem por evento utilizando o query parameter na URL.
def test_list_participantes_by_evento(client, participante_factory, evento):
    create_participante(participante_factory, evento, 2)
    evento2 = EventoFactory.create()
    create_participante(participante_factory, evento2, 1)

    url = reverse("participantes-list")
    response = client.get(url, {'evento': evento.id})
    assert response.status_code == HTTPStatus.OK
    assert len(response.json()) == 2

    response = client.get(url, {'evento': evento2.id})
    assert response.status_code == HTTPStatus.OK
    assert len(response.json()) == 1
    

#Teste para garantir que a API retorne apenas os participantes do evento solicitado
def test_detail_participante_by_evento(client, participante_factory, evento):
    evento.save()
    create_participante(participante_factory, evento, 2)
    create_participante(participante_factory, EventoFactory(), 2)
    participante = Participante.objects.filter(evento=evento).first()
    url = reverse("participantes-detail", kwargs=
                  {"pk": participante.id}) + f"?evento={evento.id}"
    response = client.get(url)
    assert response.status_code == HTTPStatus.OK
    assert uuid.UUID(response.json()['evento']) == evento.id


    #Este teste verifica se a API retorna uma lista vazia se o ID do evento solicitado não existir.
def test_list_participantes_by_noexistent_evento(client):
    url = reverse("participantes-list")+f"?evento={uuid.UUID('550e8400-e29b-11d4-a716-446655440000')}"
    response = client.get(url)
    assert response.status_code == HTTPStatus.OK
    assert len(response.json()) == 0

#teste para verificar se a API retorna um 404 se o ID do evento solicitado estiver invalido
def test_get_queryset_status_code_with_invalid_event(client):
    evento = 'Evento Inexistente'
    response = client.get('/participantes/?evento=' + evento)
    assert response.status_code == HTTPStatus.NOT_FOUND
