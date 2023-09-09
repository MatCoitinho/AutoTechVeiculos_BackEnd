from django.db import models


class Veiculo(models.Model):
    class MarcaVeiculos(models.TextChoices):
        Ford = "Ford", ("Ford")
        Toyota= "Toyota", ("Toyota")
        Honda= "Honda", ("Honda")
        Volkswagen= "VW", ("Volkswagen")
        BMW = "BMW", ("BMW")
        MercedesBenz = "MB", ("Mercedes-Benz")
        Chevrolet= "Chevy", ("Chevrolet")
        Nissan= "Nissan", ("Nissan")
        Audi= "Audi", ("Audi")
        Hyundai= "Hyundai", ("Hyundai")
        Subaru= "Subaru", ("Subaru")
        Kia= "Kia", ("Kia")
        Volvo= "Volvo", ("Volvo")
        Jaguar= "Jaguar", ("Jaguar")
        Tesla= "Tesla", ("Tesla")

    marca = models.CharField(
        max_length=13,
        choices=MarcaVeiculos.choices,
        default="undefined",
        verbose_name="Marca"
    )

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
    ano = models.DateField(verbose_name="Ano Do Modelo",)
    cambio = models.BooleanField(verbose_name="Tipo De Cambio", default=True)
    categoria = models.CharField(max_length=10, verbose_name="Categoria Carro")

    def __str__(self):
        return self.marca


class carro(models.Model):
    placa = models.CharField(max_length=7, unique = True, verbose_name = "Placa")
    quilometragem = models.CharField(max_length=7, verbose_name="Quilometragem")
    ultimaRevisao = models.DateField(verbose_name="Ultima Revisao")
    status = models.BooleanField(verbose_name="Status Do Veiculo", default=False)
    preco = models.IntegerField(verbose_name = "Preco Do Veiculo")
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)