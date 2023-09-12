from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from django.core.validators import RegexValidator


class Usuario(models.Model):
    nome =  models.CharField(max_length=100, verbose_name="Nome")
    email = models.EmailField(max_length=100, verbose_name="Email")
    cpf = models.CharField(max_length=14, unique=True, verbose_name= "CPF")
    senha = models.CharField(max_length=50)
    telefone_regex = RegexValidator(
        regex=r'^\d{10}$',  
        message="O número de telefone deve ter 10 dígitos (apenas números).",
    )
    telefone = models.CharField(validators=[telefone_regex], max_length=10, verbose_name="Telefone")
    endereco = models.CharField(max_length=300)
    admin = models.BooleanField(verbose_name="Permissao Admin")

    def __str__(self):
        return self.nome
    
    def set_password(self, senha):
        self.senha = make_password(senha)

    def check_password(self, senha):
        return check_password(senha, self.senha)