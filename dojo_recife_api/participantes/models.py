import uuid
from django.db import models
from dojo_recife_api.base.models import BaseModel


class Participante(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField("Nome", max_length=50)
    email = models.CharField("E-mail", max_length=100)
    telefone = models.CharField("Celular", max_length=11)
    documento = models.CharField("Documento", max_length=11)
    
    evento = models.ForeignKey("eventos.Evento", on_delete=models.CASCADE, null=True, blank=True,
                               related_name="participantes")

    def __str__(self):
        return self.nome
