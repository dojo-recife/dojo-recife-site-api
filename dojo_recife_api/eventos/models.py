import uuid

from django.db import models

from dojo_recife_api.base.models import BaseModel


class Evento(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    local = models.CharField("Local do Evento", max_length=255)
    data = models.DateField("Data do Evento")
    hora = models.TimeField("Horário do Evento")
    max_pessoas = models.IntegerField("Máximo de pessoas", default=0)
    data_hora_limite = models.DateTimeField("Data e hora limite para inscrição")
    
    def __str__(self):
        return f"Evento: {self.local} | {self.data} - {self.hora}"
