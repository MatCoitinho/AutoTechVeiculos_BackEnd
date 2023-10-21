from .models import Reserva
from rest_framework import serializers
from login.serializers import ClienteSerializer
from anunciarVeiculos.serializers import VeiculoSerializer


class ReservaSerializer(serializers.ModelSerializer):
    #modelo = ModeloSerializer(read_only=True)
    cliente = ClienteSerializer(read_only=True)
    veiculo = VeiculoSerializer(read_only=True)
    class Meta:
        model = Reserva
        fields = '__all__'