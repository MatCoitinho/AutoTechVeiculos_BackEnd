# from django.shortcuts import render
from rest_framework import viewsets
from .models import Modelo, Veiculo, Anuncio
from .serializers import ModeloSerializer, VeiculoSerializer, AnuncioSerializer
from django.views.decorators.csrf import csrf_exempt


class ModeloViewSet(viewsets.ModelViewSet):
    serializer_class = ModeloSerializer
    queryset = Modelo.objects.all()

class VeiculoViewSet(viewsets.ModelViewSet):
    serializer_class = VeiculoSerializer
    queryset = Veiculo.objects.all()

class AnuncioViewSet(viewsets.ModelViewSet):
    serializer_class = AnuncioSerializer
    queryset = Anuncio.objects.all()