import factory
from dojo_recife_api.participantes.models import Participante
from .eventos import EventoFactory


class ParticipanteFactory(factory.Factory):
    evento = factory.SubFactory(EventoFactory)

    nome = "Bart Simpson"
    email = "bart.simpson@gmail.com"
    telefone = "81999999999"
    documento = "11122233344"

    class Meta:
        model = Participante
