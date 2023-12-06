from django.shortcuts import render
from .serializers import VendaSerializer
from .models import Venda
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from reservarVeiculos.models import Reserva
from anunciarVeiculos.models import Veiculo, Anuncio
from django.core.mail import send_mail


class VendaViewSet(viewsets.ModelViewSet):
    serializer_class = VendaSerializer
    queryset = Venda.objects.all()
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['veiculo__modelo__model','cpf_comprador','nome_comprador']


@csrf_exempt
def criar_venda(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        cpf = data.get('cpf')
        nome = data.get('nome')
        placa = data.get('placa')
        valor = data.get('valor')
        contato = data.get('contato')

        if cpf and nome and placa and valor and contato:
            veiculo = Veiculo.objects.get(placa=placa)
            reservas = Reserva.objects.filter(veiculo = veiculo)
            anuncios = Anuncio.objects.filter(veiculo = veiculo)
            for reserva in reservas:
                email = reserva.cliente.user.username
                modelo = reserva.veiculo.modelo.model
                marca = reserva.veiculo.modelo.marca
                ano = reserva.veiculo.modelo.ano
                mensagem = f'Infelizmente sua reserva do veículo {marca} {modelo} {ano} foi cancelada pois o veículo foi vendido'
                send_mail('Autotech Veiculos-Reserva Cancelada',
                mensagem,
                'autotechveiculos3@gmail.com',
                recipient_list=[email])
                reserva.delete()
            for anuncio in anuncios:
                anuncio.delete()
            nova_venda = Venda.objects.create(cpf_comprador = cpf, nome_comprador = nome, valor = valor, contato = contato, modelo = veiculo.modelo.model, marca = veiculo.modelo.marca, ano = veiculo.modelo.ano, cor = veiculo.cor)
            nova_venda.save()
            veiculo.delete()
            return JsonResponse({'mensagem': 'Venda conclída com sucesso'}, status = 200)
        else:
            return JsonResponse({'erro': 'Dados faltando'})
    else:
        return JsonResponse({'erro': 'Metodo nao permitido'})

        
            
