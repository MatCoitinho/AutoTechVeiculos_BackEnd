from django.db import models
from django.core.exceptions import ValidationError
from login.models import Cliente
from django.views.decorators.csrf import csrf_exempt


class Modelo(models.Model):

    class TipoCombustivel(models.TextChoices):
        gasolina = "gasolina", ("Gasolina")
        alcool = "alcool", ("Alcool")
        Flex = "flex", ("Flex")
        hibrido = "hibrido", ("Híbrido")
        eletrico = "eletrico", ("Elétrico")


    tipoCombustivel = models.CharField(
        max_length=20,
        choices=TipoCombustivel.choices,
        default="Undefined", 
        verbose_name="Tipo Combustível"
    )

    def validar_data(value):
        if value < 0 or value > 10000:
            raise ValidationError("O ano deve ter no máximo 4 dígitos")

    model = models.CharField(max_length=50, verbose_name="Modelo")
    marca = models.CharField(max_length=20,verbose_name="Marca")
    ano = models.PositiveIntegerField(verbose_name="Ano",validators=[validar_data],help_text="O ano deve ter no máximo 4 dígitos")
    cambio = models.BooleanField(verbose_name="Automático", default=True)
    class CategoriaCarro(models.TextChoices):
        compacto = "compacto",("Compacto")
        seda = "sedan",("Sedan")
        suv = "suv",("SUV")
        hatchback = "hatchback",("Hatchback")
        picape = "picape",("Picape")
        esportivo = "esportivo",("Esportivo")

    categoria = models.CharField(max_length=40, verbose_name="Categoria",choices=CategoriaCarro.choices,default="Undefined")
    qtdPortas = models.IntegerField(verbose_name="Quantidade de portas")

    def __str__(self):
        return f"{self.marca} {self.model} ({self.ano})"
    
class Veiculo(models.Model):
    placa = models.CharField(max_length=7, unique = True, verbose_name = "Placa")
    quilometragem = models.CharField(max_length=7, verbose_name="Quilometragem")
    status = models.BooleanField(verbose_name="Status Do Veiculo", default=False)
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE, verbose_name="Modelo")
    dono = models.ForeignKey(Cliente, verbose_name="Dono", on_delete=models.CASCADE, null=True)
    cor = models.CharField(max_length=50, verbose_name= "Cor", default="undefined")

    def __str__(self):
        return self.placa

def upload_image(instance, filename):
    return f"{instance.veiculo}-{filename}"
class Anuncio(models.Model):
    pontos = models.IntegerField(verbose_name="Pontos", default=0)
    img1 = models.CharField(max_length=500, verbose_name="Imagem um", null=True)
    img2 = models.CharField(max_length=500, verbose_name="Imagem dois", null=True)
    descricao = models.TextField(max_length=500, verbose_name="Descricao")
    veiculo = models.ForeignKey(Veiculo, verbose_name="Veiculo", on_delete=models.CASCADE)
    destaque = models.BooleanField(verbose_name="Destaque",default=False)
    preco = models.IntegerField(verbose_name = "Preco Do Veiculo",default=0)
    servico = models.BooleanField(verbose_name="Serviço", default=False)
    
    def __str__(self):
        return self.veiculo.placa
    