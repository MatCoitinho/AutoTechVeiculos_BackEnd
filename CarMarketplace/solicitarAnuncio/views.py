from rest_framework import viewsets
from .models import Solicitacao
from .serializers import SolicitacaoSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import AllowAny


class SolicitacaoViewSet(viewsets.ModelViewSet):
    serializer_class = SolicitacaoSerializer
    queryset = Solicitacao.objects.all()
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['solicitante__cpf']
