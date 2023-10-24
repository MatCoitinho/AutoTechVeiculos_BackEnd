from .models import Modelo, Veiculo, Anuncio
from rest_framework import serializers
from login.serializers import ClienteSerializer 
class ModeloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modelo
        fields = '__all__'

class VeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veiculo
        fields = '__all__'

class AnuncioSerializer(serializers.ModelSerializer):
    modelo = serializers.CharField(source='veiculo.modelo.model',read_only=True)
    marca = serializers.CharField(source='veiculo.modelo.marca',read_only=True)
    cambio = serializers.CharField(source='veiculo.modelo.cambio',read_only=True)
    ano = serializers.CharField(source='veiculo.modelo.ano',read_only=True)
    combustivel = serializers.CharField(source='veiculo.modelo.tipoCombustivel',read_only=True)
    placa = serializers.CharField(source='veiculo.placa',read_only=True)
    cor = serializers.CharField(source='veiculo.cor',read_only=True)
    categoria = serializers.CharField(source='veiculo.modelo.categoria',read_only=True)
    portas = serializers.CharField(source='veiculo.modelo.qntdPortas',read_only=True)
    status = serializers.CharField(source='veiculo.status',read_only=True)
    dono = serializers.CharField(source='veiculo.dono.cpf',read_only=True)
    
    class Meta:
        model = Anuncio
        fields = '__all__'

