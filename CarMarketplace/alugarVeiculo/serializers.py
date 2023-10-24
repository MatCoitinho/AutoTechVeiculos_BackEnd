from .models import Alugar
from rest_framework import serializers
from login.serializers import ClienteSerializer
from anunciarVeiculos.serializers import VeiculoSerializer

class AlugarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alugar
        fields = '__all__'