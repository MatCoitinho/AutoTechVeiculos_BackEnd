from rest_framework import viewsets
from django.views.decorators.csrf import csrf_exempt
from .models import Cliente
from django.contrib.auth.models import User
from .serializers import ClienteSerializer
from django.http import JsonResponse
import json
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view

class ClienteViewSet(viewsets.ModelViewSet):
    serializer_class = ClienteSerializer
    queryset = Cliente.objects.all()
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['cpf','user__first_name']



@csrf_exempt
def Cadastrar(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        firstName = data.get('primeiroNome')
        lastName = data.get('ultimoNome')
        senha = data.get('senha')
        emails = data.get('email')
        cpfs = data.get('CPF')
        telefones = data.get('telefone')
        enderecos = data.get('endereco')

        if firstName and lastName and senha and emails and cpfs and telefones and enderecos:
           
            if User.objects.filter(username = emails).exists():
                print("Username ja existe. Escolha outro")
            else:
                user = User.objects.create_user(username=emails, first_name = firstName, last_name = lastName, password=senha, email= emails)
                cliente = Cliente.objects.create(cpf = cpfs, telefone = telefones, endereco = enderecos, user = user)
                user.save()
                cliente.save()
                print("usuario salvo")
                return JsonResponse({'mensagem': 'Usuario Cadastrado com Sucesso'},status = 200)
            
        else:
            return JsonResponse({'erro': 'Campos obrigatorios ausentes.'})
    else:
        return JsonResponse({'erro': 'Metodo nao permitido.'})
    


@csrf_exempt
@api_view(['POST'])
def Logar(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        email = data.get('email')
        password = data.get('password')
        user = authenticate(request, username=email, password = password)

        if user:
            refresh = RefreshToken.for_user(user)
            if user.is_superuser:
                return Response({
                    'token': str(refresh.access_token),
                    'user': {
                        'id': user.id,
                        'name' : user.first_name,
                        'email': user.username,
                        'phone': '',
                        'cpf': '',
                        'address': '',
                        'is_superuser': user.is_superuser,
                    },
                })
            else:
                cliente = Cliente.objects.get(user = user)
                return Response({
                    'token': str(refresh.access_token),
                    'user': {
                        'id': cliente.id,
                        'name' : user.first_name,
                        'email': user.username,
                        'phone': cliente.telefone,
                        'cpf': cliente.cpf,
                        'address': cliente.endereco,
                        'is_superuser': user.is_superuser,
                    },
                })
        else:
            return JsonResponse({'erro': 'Credenciais inválidas'}, status=400)
        
    else:
        return JsonResponse({'erro':'Metodo nao permitido'})


@csrf_exempt
@api_view(['POST'])
def retrieveUserCliente(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        email = data.get('email')

        if email:
            user = User.objects.get(username = email)
            if user.is_superuser:
                return Response({
                    'id': user.id,
                    'name' : user.first_name,
                    'email': user.username,
                    'phone': '',
                    'cpf': '',
                    'address': '',
                    'is_superuser': user.is_superuser,
                })
            else:
                cliente = Cliente.objects.get(user=user)
                return Response({
                    'id': cliente.id,
                    'name' : user.first_name,
                    'email': user.username,
                    'phone': cliente.telefone,
                    'cpf': cliente.cpf,
                    'address': cliente.endereco,
                    'is_superuser': user.is_superuser,
                })
        else:
            return Response({'erro': 'Erro'})
    else:
        return Response({'erro': 'Metodo inválido'})










