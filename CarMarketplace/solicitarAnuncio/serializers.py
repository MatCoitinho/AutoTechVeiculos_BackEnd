from .models import Solicitacao
from rest_framework import serializers

class SolicitacaoSerializer(serializers.ModelSerializer):
    dono_cpf = serializers.CharField(source='solicitante.cpf',read_only=True)
    dono_email = serializers.CharField(source='solicitante.user.email',read_only=True)
    dono_name = serializers.CharField(source='solicitante.user.first_name',read_only=True)
    dono_telefone = serializers.CharField(source='solicitante.telefone',read_only=True)
    class Meta:
        model = Solicitacao
        fields = '__all__'