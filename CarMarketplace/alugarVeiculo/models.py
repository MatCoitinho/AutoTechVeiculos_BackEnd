from django.db import models
from login.models import Cliente
from anunciarVeiculos.models import Veiculo

class Alugar(models.Model):
    cliente = models.ForeignKey(Cliente, verbose_name="Cliente", on_delete=models.CASCADE)
    veiculo = models.ForeignKey(Veiculo, verbose_name="Veiculo", on_delete=models.CASCADE)
    dataInicio = models.DateField(verbose_name="Data da retirada",null=True) 
    dataDev = models.DateField(verbose_name="Data de devolução",null=True)