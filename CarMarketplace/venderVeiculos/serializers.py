from .models import Venda
from rest_framework import serializers

class VendaSerializer(serializers.ModelSerializer):
    tipoCombustivel = serializers.CharField(source='veiculo.modelo.tipoCombustivel', read_only=True)
    model= serializers.CharField(source='veiculo.modelo.model', read_only=True)
    marca= serializers.CharField(source='veiculo.modelo.marca', read_only=True)
    ano= serializers.CharField(source='veiculo.modelo.ano', read_only=True)
    cambio= serializers.CharField(source='veiculo.modelo.cambio', read_only=True)
    categoria= serializers.CharField(source='veiculo.modelo.categoria', read_only=True)
    qtdPortas= serializers.CharField(source='veiculo.modelo.qtdPortas', read_only=True)
    placa = serializers.CharField(source='veiculo.placa',read_only=True)
    class Meta:
        model = Venda
        fields = '__all__'