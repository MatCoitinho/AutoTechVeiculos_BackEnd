from django.shortcuts import render
from rest_framework import viewsets
from .models import Modelo, Veiculo, Anuncio
from .serializers import ModeloSerializer, VeiculoSerializer, AnuncioSerializer
from rest_framework.permissions import AllowAny
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
import json
from login.models import Cliente

class ModeloViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = ModeloSerializer
    queryset = Modelo.objects.all()

class VeiculoViewSet(viewsets.ModelViewSet):
    serializer_class = VeiculoSerializer
    queryset = Veiculo.objects.all()
    permission_classes = [AllowAny]

class AnuncioViewSet(viewsets.ModelViewSet):
    serializer_class = AnuncioSerializer
    queryset = Anuncio.objects.all().order_by('-destaque','-pontos')

@csrf_exempt
def criarVeiculo(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        placa = data.get('placa')
        quilometragem = data.get('quilometragem')
        status = data.get('status')
        cor = data.get('cor')
        modelo = data.get('modelo')
        ano = data.get('ano')
        dono = data.get('dono')

        if placa and quilometragem and cor and modelo and ano:
            if Veiculo.objects.filter(placa = placa).exists():
                print("Veiculo ja existe")
                return JsonResponse({'mensagem': 'Já existe um veiculo cadastrado com esta placa'})
            else:
                modelo_veiculo = Modelo.objects.get(model = modelo, ano = ano)
                dono_veiculo = Cliente.objects.get(cpf=dono)
                novo_veiculo = Veiculo.objects.create(placa = placa, quilometragem = quilometragem, status = status, cor = cor, modelo = modelo_veiculo, dono = dono_veiculo)
                novo_veiculo.save()
                print("Veiculo cadastrado com sucesso")
                return JsonResponse({'mensagem': 'Veiculo criado com sucesso'}, status=200)
        else:
            print("Campo faltando")
            return JsonResponse({'erro':'Campos Obrigatorios ausentes'})
    else:
        print("Metodo errado")
        return JsonResponse({'erro':'Metodo nao permitido.'})
    

@csrf_exempt
def criarAnuncio(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        pontos = data.get('pontos')
        img1 = data.get('img1')
        img2 = data.get('img2')
        descricao = data.get('descricao')
        placa = data.get('placa')
        destaque = data.get('destaque')
        preco = data.get('preco')
        servico = data.get('servico')

        if pontos and img1 and img2 and descricao and placa and preco:
            veic = Veiculo.objects.get(placa=placa)
            if Anuncio.objects.filter(veiculo = veic, servico = servico).exists():
                print("Ja existe um anuncio desse tipo de servico para esse veiculo")
                return JsonResponse({'mensagem': 'Ja existe um anuncio desse tipo de servico para esse veiculo'})
            else:
                veiculo_anuncio = Veiculo.objects.get(placa=placa)
                novo_anuncio = Anuncio.objects.create(pontos = pontos, img1 = img1, img2 = img2, descricao = descricao, veiculo = veiculo_anuncio, destaque = destaque, preco = preco, servico = servico)
                novo_anuncio.save()
                print("Anuncio criado com sucesso")
                return JsonResponse({'mensagem': 'Anuncio criado com sucesso'}, status=200)
        else:
            print("Campo faltando")
            return JsonResponse({'erro':'Campos Obrigatorios ausentes'})
    else:
        print("Metodo errado")
        return JsonResponse({'erro':'Metodo nao permitido.'})