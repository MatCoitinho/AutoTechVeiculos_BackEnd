from .models import Solicitacao
from rest_framework import serializers

class SolicitacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solicitacao
        fields = '__all__'