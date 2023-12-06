from django.db import models
from login.models import Cliente
from anunciarVeiculos.models import Veiculo

class Reserva(models.Model):
    cliente = models.ForeignKey(Cliente, verbose_name="Cliente",on_delete=models.CASCADE)
    veiculo = models.ForeignKey(Veiculo,verbose_name="Veiculo Reservado",on_delete=models.CASCADE)
    data = models.CharField(verbose_name="Data da Visita",null=True,max_length=200)
    hora = models.CharField(verbose_name="Hora da visita",null=True,max_length=200)
   
