from uuid import UUID


def test_simple_evento(evento):
    assert evento
    assert isinstance(evento.id, UUID)
