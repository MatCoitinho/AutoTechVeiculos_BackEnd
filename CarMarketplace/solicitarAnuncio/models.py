from django.db import models
from login.models import Usuario


class Solicitacao(models.Model):
    marca = models.CharField(max_length=50, verbose_name="Marca")
    modelo = models.CharField(max_length=50, verbose_name="Modelo")
    ano = models.CharField(max_length=4, verbose_name="Ano")
    quilometragem = models.CharField(max_length=6, verbose_name="Quilometragem")
    cambio = models.BooleanField(verbose_name="Automático",default=False)
    data = models.DateField(verbose_name="Data", auto_now_add=True)
    servico = models.BooleanField(verbose_name="Alugar?",default=False)
    solicitante = models.ForeignKey(Usuario, verbose_name="Solicitante", null= True, on_delete=models.CASCADE)

    class Combustivel(models.TextChoices):
        gasolina = "Gasol", ("Gasolina")
        alcool = "alco", ("Alcool")
        Flex = "Flex", ("Flex")
    
    tipocombust = models.CharField(
        max_length=20,
        choices=Combustivel.choices,
        default="Undefined",
        verbose_name="Combustível"
    )
