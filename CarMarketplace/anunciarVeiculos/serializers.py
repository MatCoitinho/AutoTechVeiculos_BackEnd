from .models import Modelo, Veiculo
from rest_framework import serializers

class ModeloSerializer(serializers.HyperlinkedModelSerializer):
    class meta:
        model = Modelo
        fields = ['id','tipoCombustivel','modelo','marca','ano','cambio','categoria','qtdPortas']

class VeiculoSerializer(serializers.ModelSerializer):
    class meta:
        model = Veiculo
        fields = ['id','placa','quilometragem','ultimaRevisao','status','preco','veiculo']
