from datetime import date, time, datetime
from http import HTTPStatus
import pytest
from pytest_factoryboy.fixture import register
from tests.factories.eventos import EventoFactory
from rest_framework.reverse import reverse

pytestmark = pytest.mark.django_db

register(EventoFactory, "another_evento")


def create_evento(evento_factory, amount=1):
    for _ in range(amount):
        evento_factory().save()


def test_list_eventos(client, evento_factory):
    create_evento(evento_factory, 2)
    url = reverse("evento-list")
    response = client.get(url)
    assert response.status_code == HTTPStatus.OK
    assert len(response.json()) == 2


def test_create_evento(client, evento_payload):
    url = reverse("evento-list")
    response = client.post(url, evento_payload)
    assert response.status_code == HTTPStatus.CREATED


@pytest.mark.parametrize(
    "field", ["local", "data", "hora", "data_hora_limite"]
)
def test_create_evento_without_field(field, client, evento_payload):
    evento_payload.pop(field)
    url = reverse("evento-list")
    response = client.post(url, evento_payload)
    assert response.status_code == HTTPStatus.BAD_REQUEST


@pytest.mark.parametrize(
    "field", ["local", "data", "hora", "data_hora_limite"]
)
def test_create_evento_with_field_blank(field, client, evento_payload):
    evento_payload[field] = ""
    url = reverse("evento-list")
    response = client.post(url, evento_payload)
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_detail_evento(client, evento):
    evento.save()
    url = reverse("evento-detail", kwargs={"pk": evento.id})
    response = client.get(url)
    assert response.status_code == HTTPStatus.OK


def test_detail_evento_nonexistent(client):
    url = reverse("evento-detail", kwargs={"pk": 123})
    response = client.get(url)
    assert response.status_code == HTTPStatus.NOT_FOUND


def test_update_evento(client, evento):
    evento.save()
    url = reverse("evento-detail", kwargs={"pk": evento.id})
    payload = {
        "local": "Novo Local",
        "data": date(2023, 4, 15),
        "hora": time(20),
        "max_pessoas": 20,
        "data_hora_limite": datetime(2023, 4, 15, 14),
    }
    response = client.put(url, payload, content_type="application/json")

    assert response.status_code == HTTPStatus.OK
    assert str(evento.id) == response.json()["id"]
    assert evento.local != response.json()["local"]
    assert evento.data != response.json()["data"]
    assert evento.hora != response.json()["hora"]
    assert evento.max_pessoas != response.json()["max_pessoas"]
    assert evento.data_hora_limite != response.json()["data_hora_limite"]


def test_fail_update_evento(client, evento):
    evento.save()
    url = reverse("evento-detail", kwargs={"pk": evento.id})
    payload = {
        "local": "Novo Local",
    }
    response = client.put(url, payload, content_type="application/json")

    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_partial_update_evento(client, evento):
    evento.save()
    url = reverse("evento-detail", kwargs={"pk": evento.id})
    payload = {"local": "Novo Local"}
    response = client.patch(url, payload, content_type="application/json")

    assert response.status_code == HTTPStatus.OK
    assert evento.local != response.json()["local"]
