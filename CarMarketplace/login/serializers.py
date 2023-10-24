from .models import Cliente
from rest_framework import serializers

class ClienteSerializer(serializers.ModelSerializer):
    cliente_email = serializers.CharField(source='user.email',read_only=True)
    cliente_firstName = serializers.CharField(source='user.first_name',read_only=True)
    cliente_lastName = serializers.CharField(source='user.last_name',read_only=True)

    class Meta:
        model = Cliente
        fields = '__all__'

