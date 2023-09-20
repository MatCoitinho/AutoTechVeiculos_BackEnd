# from django.shortcuts import render
from rest_framework import viewsets
from .models import Modelo, Veiculo, Anuncio
from .serializers import ModeloSerializer, VeiculoSerializer, AnuncioSerializer
from rest_framework.permissions import AllowAny


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
    queryset = Anuncio.objects.all()