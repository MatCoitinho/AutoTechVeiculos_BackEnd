from .models import Reserva
from rest_framework import serializers
from login.serializers import ClienteSerializer
from anunciarVeiculos.serializers import VeiculoSerializer


class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'