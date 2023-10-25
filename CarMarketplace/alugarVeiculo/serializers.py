from .models import Alugar
from rest_framework import serializers
from login.serializers import ClienteSerializer
from anunciarVeiculos.serializers import VeiculoSerializer

class AlugarSerializer(serializers.ModelSerializer):
    cliente_email = serializers.CharField(source='cliente.user.email',read_only=True)
    cliente_firstName = serializers.CharField(source='cliente.user.first_name',read_only=True) 
    cliente_lastName = serializers.CharField(source='cliente.user.last_name',read_only=True)
    cpf = serializers.CharField(source='cliente.cpf',read_only=True)
    telefone = serializers.CharField(source='cliente.telefone',read_only=True)
    endereco = serializers.CharField(source='cliente.endereco',read_only=True)

    tipoCombustivel = serializers.CharField(source='veiculo.modelo.tipoCombustivel', read_only=True)
    model= serializers.CharField(source='veiculo.modelo.model', read_only=True)
    marca= serializers.CharField(source='veiculo.modelo.marca', read_only=True)
    ano= serializers.CharField(source='veiculo.modelo.ano', read_only=True)
    cambio= serializers.CharField(source='veiculo.modelo.cambio', read_only=True)
    categoria= serializers.CharField(source='veiculo.modelo.categoria', read_only=True)
    qtdPortas= serializers.CharField(source='veiculo.modelo.qtdPortas', read_only=True)
    class Meta:
        model = Alugar
        fields = '__all__'