from django.db import models
from login.models import Cliente
from anunciarVeiculos.models import Veiculo

class Alugar(models.Model):
    cliente = models.ForeignKey(Cliente, verbose_name="Cliente", on_delete=models.CASCADE)
    veiculo = models.ForeignKey(Veiculo, verbose_name="Veiculo", on_delete=models.CASCADE)
    dataInicio = models.CharField(verbose_name="Data da retirada",null=True,max_length=200)
    hora_retirada = models.CharField(verbose_name="Hora da retirada",null=True,max_length=200) 
    dataDev = models.CharField(verbose_name="Data de devolução",null=True,max_length=200)