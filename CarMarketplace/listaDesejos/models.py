from django.db import models
from django.core.exceptions import ValidationError
from login.models import Cliente


def validar_data(value):
    if value < 0 or value > 10000:
        raise ValidationError("O ano deve ter no máximo 4 dígitos")

class Desejo(models.Model):
    modelo = models.CharField(max_length=50, verbose_name="Modelo")
    marca = models.CharField(max_length=50, verbose_name="Marca")
    ano = models.IntegerField(verbose_name="Ano",validators=[validar_data],help_text="O ano deve ter no máximo 4 dígitos")
    dono = models.ForeignKey(Cliente, verbose_name="Dono", on_delete=models.CASCADE, null=True)    




