from django.db import models
from anunciarVeiculos.models import Veiculo

# Create your models here.
class Venda(models.Model):
    nome_comprador = models.CharField(max_length=200,verbose_name="Nome completo do comprador")
    cpf_comprador = models.CharField(max_length=11,verbose_name="CPF")
    data = models.DateField(auto_now_add=True)
    veiculo = models.ForeignKey(Veiculo,on_delete=models.CASCADE,verbose_name="Placa do veículo comprado")
    valor = models.IntegerField(verbose_name="Preço pago")
    