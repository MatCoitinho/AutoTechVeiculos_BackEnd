from django.shortcuts import render
from .models import Alugar
from .serializers import AlugarSerializer
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from login.models import Cliente
from django.contrib.auth.models import User
from anunciarVeiculos.models import Veiculo, Anuncio


class AlugarViewSet(viewsets.ModelViewSet):
    serializer_class = AlugarSerializer
    queryset = Alugar.objects.all()
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['veiculo__modelo__model','cliente__cpf']

@csrf_exempt
def criarAluguel(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        email = data.get('email')
        veic = data.get('id')
        dataInicio = data.get('inicio')
        dataDev = data.get('fim')
        hora = data.get('hora')

        if email and veic:
            user = User.objects.get(username = email)
            cliente = Cliente.objects.get(user=user)
            anuncio = Anuncio.objects.get(id=veic)
            veiculo = Veiculo.objects.get(id=anuncio.veiculo.id)
            novo_aluguel = Alugar.objects.create(cliente = cliente, veiculo = veiculo,dataInicio = dataInicio, dataDev = dataDev, hora_retirada = hora)
            novo_aluguel.save()
            anuncio.delete()
            return JsonResponse({'mensagem': 'Aluguel feito com sucesso'})
        else:
            return JsonResponse({'erro': 'Campos Faltando'})
    else:
        return JsonResponse({'erro': 'Metodo nao permitido'})