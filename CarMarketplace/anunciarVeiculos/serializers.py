from .models import Modelo, Veiculo, Anuncio
from rest_framework import serializers

class ModeloSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Modelo
        fields = ["id","tipoCombustivel","model","marca","ano","cambio","categoria","qtdPortas"]

class VeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veiculo
        fields = ["id","placa","quilometragem","status","preco","veiculo","servico","dono","cor"]

class AnuncioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anuncio
        fields = ["id","pontos","img1","img2","descricao","veiculo"]