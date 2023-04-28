import pytest


@pytest.fixture
def participante_payload(participante):
    return {
        "nome": participante.nome,
        "email": participante.email,
        "telefone": participante.telefone,
        "documento": participante.documento,
        "evento": str(participante.evento.id),
    }
