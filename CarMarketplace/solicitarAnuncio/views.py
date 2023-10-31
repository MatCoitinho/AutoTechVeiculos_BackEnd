from rest_framework import viewsets
from .models import Solicitacao
from .serializers import SolicitacaoSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import AllowAny
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from login.models import Cliente
from django.contrib.auth.models import User




class SolicitacaoViewSet(viewsets.ModelViewSet):
    serializer_class = SolicitacaoSerializer
    queryset = Solicitacao.objects.all()
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['solicitante__cpf','situacao']

@csrf_exempt
def criarSolicitacao(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        solicitante = data.get('solicitante')
        marca = data.get('marca')
        modelo = data.get('modelo')
        ano = data.get('ano')
        quilometragem = data.get('quilometragem')
        cambio = data.get('cambio')
        servico = data.get('servico')
        combustivel = data.get('combustivel')

        if solicitante and marca and modelo and ano and quilometragem and cambio and servico and combustivel:
            user = User.objects.get(username = solicitante)
            cliente = Cliente.objects.get(user=user)
            nova_solicitacao = Solicitacao.objects.create(marca = marca, modelo = modelo, ano = ano, quilometragem = quilometragem, cambio = cambio, servico = servico, solicitante = cliente, combustivel=combustivel, situacao = False)
            nova_solicitacao.save()
            return JsonResponse({'mensagem': 'Solicitacao enviada'}, status = 200)
        else:
            return JsonResponse({'erro': 'Falta campos obrigatorios'})
    else:
        return JsonResponse({'erro': 'Metodo nao permitido'})