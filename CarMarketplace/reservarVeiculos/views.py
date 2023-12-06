from django.shortcuts import render
from .models import Reserva
from .serializers import ReservaSerializer
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from login.models import Cliente
from django.contrib.auth.models import User
from anunciarVeiculos.models import Veiculo, Anuncio


class ReservaViewSet(viewsets.ModelViewSet):
    serializer_class = ReservaSerializer
    queryset = Reserva.objects.all()
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['veiculo__modelo__model','cliente__cpf']

@csrf_exempt
def criarReserva(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        client = data.get('email')
        veic = data.get('id')
        dia = data.get('dia')
        hora = data.get('hora')

        if client and veic:
            user = User.objects.get(username = client)
            cliente = Cliente.objects.get(user=user)
            anuncio = Anuncio.objects.get(id=veic)
            veiculo = Veiculo.objects.get(id=anuncio.veiculo.id)
            nova_reserva = Reserva.objects.create(cliente = cliente, veiculo = veiculo,data = dia, hora = hora)
            nova_reserva.save()
            return JsonResponse({'mensagem': 'Reserva feita com sucesso'})
        else:
            return JsonResponse({'erro': 'Dados faltando'})
    else:
        return JsonResponse({'erro': 'Metodo invalido'})