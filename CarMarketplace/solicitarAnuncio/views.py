from rest_framework import viewsets
from .models import Solicitacao
from .serializers import SolicitacaoSerializer

class SolicitacaoViewSet(viewsets.ModelViewSet):
    serializer_class = SolicitacaoSerializer
    queryset = Solicitacao.objects.all()
