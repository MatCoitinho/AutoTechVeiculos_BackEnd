from django.db import models


class Modelo(models.Model):

    class TipoCombustivel(models.TextChoices):
        gasolina = "Gasol", ("Gasolina")
        alcool = "alco", ("Alcool")
        Flex = "Flex", ("Flex")

    tipoCombustivel = models.CharField(
        max_length=20,
        choices=TipoCombustivel.choices,
        default="undefined", 
        verbose_name="Tipo Combustivel"
    )

    modelo = models.CharField(max_length=50, verbose_name="modelo")
    marca = models.CharField(max_length=20,verbose_name="marca")
    ano = models.DateField(verbose_name="Ano Do Modelo",)
    cambio = models.BooleanField(verbose_name="Tipo De Cambio", default=True)
    categoria = models.CharField(max_length=10, verbose_name="Categoria Carro")
    qtdPortas = models.IntegerField(verbose_name="quantidade de portas")

    def __str__(self):
        return self.marca


class Veiculo(models.Model):
    placa = models.CharField(max_length=7, unique = True, verbose_name = "Placa")
    quilometragem = models.CharField(max_length=7, verbose_name="Quilometragem")
    ultimaRevisao = models.DateField(verbose_name="Ultima Revisao")
    status = models.BooleanField(verbose_name="Status Do Veiculo", default=False)
    preco = models.IntegerField(verbose_name = "Preco Do Veiculo")
    veiculo = models.ForeignKey(Modelo, on_delete=models.CASCADE)