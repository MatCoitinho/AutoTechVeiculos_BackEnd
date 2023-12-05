from django.db import models
from anunciarVeiculos.models import Veiculo

# Create your models here.
class Venda(models.Model):
    nome_comprador = models.CharField(max_length=200,verbose_name="Nome completo do comprador")
    cpf_comprador = models.CharField(max_length=11,verbose_name="CPF")
    data = models.DateField(auto_now_add=True)
    modelo = models.CharField(max_length=100, verbose_name='Modelo',null=True)
    marca = models.CharField(max_length=100, verbose_name='Marca',null=True)
    ano = models.IntegerField(verbose_name='Ano',null=True)
    cor = models.CharField(max_length=100,verbose_name='Cor',null=True)
    valor = models.IntegerField(verbose_name="Preço pago")
    contato = models.CharField(verbose_name='Contato do comprador',max_length=100,null=True)
    