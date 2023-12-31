from django.db import models
from login.models import Cliente
from django.contrib.auth.models import User

class Solicitacao(models.Model):
    marca = models.CharField(max_length=50, verbose_name="Marca")
    modelo = models.CharField(max_length=50, verbose_name="Modelo")
    ano = models.CharField(max_length=4, verbose_name="Ano")
    quilometragem = models.CharField(max_length=6, verbose_name="Quilometragem")
    cambio = models.CharField(verbose_name="Câmbio",max_length=50)
    data = models.DateField(auto_now_add=True)
    servico = models.CharField(verbose_name="Serviço",max_length=50)
    solicitante = models.ForeignKey(Cliente, verbose_name="Solicitante", null= True, on_delete=models.CASCADE)
    combustivel = models.CharField(verbose_name="Combustível",max_length=50,default="Gasolina")
    situacao = models.BooleanField(verbose_name="Situação",default=False)
