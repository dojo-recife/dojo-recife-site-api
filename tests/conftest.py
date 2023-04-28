from typing import Callable
import pytest
from pytest_factoryboy import register
from tests.factories.eventos import EventoFactory
from tests.factories.participantes import ParticipanteFactory


register(EventoFactory)
register(ParticipanteFactory)
