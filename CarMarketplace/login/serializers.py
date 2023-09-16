
from .models import Cliente
from django.contrib.auth.models import User

from rest_framework import serializers

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:

        model = Cliente
        fields = ["id","cpf", "telefone", "endereco","user"]

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = '__all__'
