from rest_framework import viewsets

from .models import Cliente
from django.contrib.auth.models import User
from .serializers import ClienteSerializer, UserSerializer
from django.http import JsonResponse
import json
class ClienteViewSet(viewsets.ModelViewSet):
    serializer_class = ClienteSerializer
    queryset = Cliente.objects.all()

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

def Cadastrar(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        usname = data.get('username')
        firstName = data.get('primeiroNome')
        lastName = data.get('ultimoNome')
        senha = data.get('senha')
        emails = data.get('email')
        cpfs = data.get('CPF')
        telefones = data.get('telefone')
        enderecos = data.get('endereco')

        if usname and firstName and lastName and senha and emails and cpfs and telefones and enderecos:
            try:
                if User.objects.filter(username = usname).exists():
                    print("Username ja existe. Escolha outro")
                else:
                    user = User.objects.create_user(username=usname, first_name = firstName, last_name = lastName, password=senha, email= emails)
                    cliente = Cliente.objects.create(cpf = cpfs, telefone = telefones, endereco = enderecos)
                    user.save()
                    cliente.save()
                    return JsonResponse({'mensagem': 'Usuario Cadastrado com Sucesso'})
                
            except Exception as e:
                return JsonResponse({'erro': str(e)})
        else:
            return JsonResponse({'erro': 'Campos obrigatorios ausentes.'})
    else:
        return JsonResponse({'erro': 'Metodo nao permitido.'})






