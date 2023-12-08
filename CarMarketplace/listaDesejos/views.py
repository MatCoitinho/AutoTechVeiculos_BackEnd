from django.shortcuts import render
from .models import Desejo
from .serializers import DesejoSerializer
from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .models import Cliente
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.models import User



class DesejoViewSet(viewsets.ModelViewSet):
    serializer_class = DesejoSerializer
    queryset = Desejo.objects.all()
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['dono__user__username']


@csrf_exempt
@api_view(['POST'])
def adicionarDesejo(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        email = data.get('email')
        modelo = data.get('modelo')
        marca = data.get('marca')
        ano = data.get('ano')

        user = User.objects.get(username = email)
        cliente = Cliente.objects.get(user = user)
        if cliente and modelo and marca and ano:
            novo_desejo = Desejo.objects.create(dono = cliente, modelo = modelo, marca = marca, ano = ano)
            novo_desejo.save()
            return JsonResponse({'mensagem': 'Objeto adicionado a lista de desejo'}, status=200)
        else:
            return JsonResponse({'erro': 'Dados faltando'})
    else:
        return JsonResponse({'erro': 'Metodo nao permitido'})



        