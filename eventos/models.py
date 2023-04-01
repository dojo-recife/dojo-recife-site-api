from django.db import models


class Eventos(models.Model):
    local = models.CharField("Local do Evento", max_length=255)
    data_hora = models.DateTimeField("Data e Hora do Evento")
    max_pessoas = models.IntegerField("Máximo de pessoas", default=0)
    data_hora_limite = models.DateTimeField("Data e hora limite para inscrição")

    inscritos = models.ManyToManyField("participantes.Participantes")

    def __str__(self):
        return f"Evento {self.local} no dia {self.data_hora}"
