from django.db import models


class SolicitacaoSala(models.Model):
    horario = models.DateTimeField()
    solicitante = models.CharField(max_length=100)
    sala = models.ForeignKey("Sala", on_delete=models.CASCADE, related_name="sala")
    