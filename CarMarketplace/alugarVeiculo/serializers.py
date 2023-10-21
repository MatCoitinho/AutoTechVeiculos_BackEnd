from .models import Alugar
from rest_framework import serializers
from login.serializers import ClienteSerializer
from anunciarVeiculos.serializers import VeiculoSerializer

class AlugarSerializer(serializers.ModelSerializer):
    veiculo = VeiculoSerializer(read_only=True)
    cliente = ClienteSerializer(read_only=True)
    class Meta:
        model = Alugar
        fields = '__all__'