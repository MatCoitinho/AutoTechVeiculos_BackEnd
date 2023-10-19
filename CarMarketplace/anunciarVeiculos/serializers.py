from .models import Modelo, Veiculo, Anuncio
from rest_framework import serializers
from login.serializers import ClienteSerializer 
class ModeloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modelo
        fields = ["id","tipoCombustivel","model","marca","ano","cambio","categoria","qtdPortas"]

class VeiculoSerializer(serializers.ModelSerializer):
    modelo = ModeloSerializer(read_only=True)
    dono = ClienteSerializer(read_only=True)
    class Meta:
        model = Veiculo
        fields = ["id","placa","quilometragem","status","modelo","dono","cor"]

class AnuncioSerializer(serializers.ModelSerializer):
    veiculo = VeiculoSerializer(read_only=True)
    class Meta:
        model = Anuncio
        fields = ["id","pontos","img1","img2","descricao","veiculo","destaque","preco","servico"]

