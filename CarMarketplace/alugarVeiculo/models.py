from django.db import models
from login.models import Cliente
from anunciarVeiculos.models import Veiculo

class Alugar(models.Model):
    cliente = models.ForeignKey(Cliente, verbose_name="Cliente", on_delete=models.CASCADE)
    veiculo = models.ForeignKey(Veiculo, verbose_name="Veiculo", on_delete=models.CASCADE)
    data = models.DateField(verbose_name="Data da visita") 
    horario = models.TimeField(verbose_name="Hora da visita")