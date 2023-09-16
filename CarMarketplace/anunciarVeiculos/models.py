from django.db import models
from django.contrib.auth.models import User


class Modelo(models.Model):

    class TipoCombustivel(models.TextChoices):
        gasolina = "Gasol", ("Gasolina")
        alcool = "alco", ("Alcool")
        Flex = "Flex", ("Flex")

    tipoCombustivel = models.CharField(
        max_length=20,
        choices=TipoCombustivel.choices,
        default="Undefined", 
        verbose_name="Tipo Combustível"
    )

    model = models.CharField(max_length=50, verbose_name="Modelo")
    marca = models.CharField(max_length=20,verbose_name="Marca")
    ano = models.DateField(verbose_name="Ano Do Modelo",)
    cambio = models.BooleanField(verbose_name="Tipo De Cambio", default=True)
    categoria = models.CharField(max_length=10, verbose_name="Categoria Carro")
    qtdPortas = models.IntegerField(verbose_name="Quantidade de portas")

    def __str__(self):
        return self.model

class Veiculo(models.Model):
    placa = models.CharField(max_length=7, unique = True, verbose_name = "Placa")
    quilometragem = models.CharField(max_length=7, verbose_name="Quilometragem")
    status = models.BooleanField(verbose_name="Status Do Veiculo", default=False)
    preco = models.IntegerField(verbose_name = "Preco Do Veiculo")
    veiculo = models.ForeignKey(Modelo, on_delete=models.CASCADE, verbose_name="Modelo/Marca")
    servico = models.BooleanField(verbose_name="Serviço", default=False)
    dono = models.ForeignKey(User, verbose_name="Dono", on_delete=models.CASCADE, null=True)
    cor = models.CharField(max_length=50, verbose_name= "Cor", default="undefined")

    def __str__(self):
        return self.placa



class Anuncio(models.Model):
    pontos = models.IntegerField(verbose_name="Pontos")
    img1 = models.CharField(max_length=100, verbose_name="Imagem um")
    img2 = models.CharField(max_length=100, verbose_name="Imagem dois")
    descricao = models.TextField(max_length=300, verbose_name="Descricao")
    veiculo = models.ForeignKey(Veiculo, verbose_name="Veiculo", on_delete=models.CASCADE)

    def __str__(self):
        return self.veiculo.placa