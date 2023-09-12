from .models import Modelo, Veiculo, Anuncio
from rest_framework import serializers

class ModeloSerializer(serializers.HyperlinkedModelSerializer):
    class meta:
        model = Modelo
        fields = ['id','tipoCombustivel','modelo','marca','ano','cambio','categoria','qtdPortas']

class VeiculoSerializer(serializers.ModelSerializer):
    class meta:
        model = Veiculo
        fields = ['id','placa','quilometragem','status','preco','veiculo','servico','dono']

class AnuncioSerializer(serializers.ModelSerializer):
    class meta:
        model = Anuncio
        fields = ['id','pontos','img1','img2','descricao','veiculo']