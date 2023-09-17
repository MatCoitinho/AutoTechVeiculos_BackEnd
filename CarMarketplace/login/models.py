from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User


class Cliente(models.Model):
    cpf = models.CharField(max_length=14, unique=True, verbose_name= "CPF")
    telefone_regex = RegexValidator(
        regex=r'^\d{11}$',  
        message="O número de telefone deve ter 11 dígitos (apenas números).",
    )
    telefone = models.CharField(validators=[telefone_regex], max_length=11, verbose_name="Telefone")
    endereco = models.CharField(max_length=300)

    user = models.ForeignKey(User,on_delete=models.CASCADE, unique=True,null=True)


    def __str__(self):
        return self.cpf