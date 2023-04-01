from django.db import models


class Participantes(models.Model):
    nome = models.CharField("Nome", max_length=50)
    email = models.CharField("E-mail", max_length=100)
    telefone = models.CharField("Celular", max_length=11)
    documento = models.CharField("Documento", max_length=11)
    
    evento = models.ForeignKey("eventos.Eventos", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nome
