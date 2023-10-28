from rest_framework import viewsets
from .models import Solicitacao
from .serializers import SolicitacaoSerializer
from django_filters.rest_framework import DjangoFilterBackend

class SolicitacaoViewSet(viewsets.ModelViewSet):
    serializer_class = SolicitacaoSerializer
    queryset = Solicitacao.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['solicitante__cpf']
