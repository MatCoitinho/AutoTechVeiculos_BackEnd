from .models import Veiculo, carro
from rest_framework import serializers

class VeiculoSerializer(serializers.HyperlinkedModelSerializer):
    class meta:
        model = Veiculo
        fields = ['id','marca','tipoCombustivel','modelo','ano','cambio','categoria']

class carroSerializer(serializers.ModelSerializer):
    class meta:
        model = carro
        fields = ['id','placa','quilometragem','ultimaRevisao','status','preco','veiculo']
