from .models import Usuario
from rest_framework import serializers

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields: ["id", "nome", "CPF","Email", "Telefone", "Endereço", "Senha", "Admin"]