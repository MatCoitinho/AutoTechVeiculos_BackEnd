from .models import Solicitacao
from rest_framework import serializers

class SolicitacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solicitacao
        fields = ["id", "marca", "modelo", "ano", "quilometragem", "cambio", "data", "servico", "tipocombust", "solicitante"]