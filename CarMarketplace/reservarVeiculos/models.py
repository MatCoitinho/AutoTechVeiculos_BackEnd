from django.db import models
from login.models import Cliente
from anunciarVeiculos.models import Veiculo

class Reserva(models.Model):
    cliente = models.ForeignKey(Cliente, verbose_name="Cliente",on_delete=models.CASCADE)
    veiculo = models.ForeignKey(Veiculo,verbose_name="Veiculo Reservado",on_delete=models.CASCADE)
