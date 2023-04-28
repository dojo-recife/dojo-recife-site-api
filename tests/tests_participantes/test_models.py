from uuid import UUID


def test_simple_participante(participante):
    assert participante
    assert isinstance(participante.id, UUID)
