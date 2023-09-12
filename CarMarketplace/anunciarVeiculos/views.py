# from django.shortcuts import render
from rest_framework import viewsets
from .models import Modelo, Veiculo
from .serializers import ModeloSerializer, VeiculoSerializer


class ModeloViewSet(viewsets.ModelViewSet):
    serializer_class = ModeloSerializer
    queryset = Modelo.objects.all()

class VeiculoViewSet(viewsets.ModelViewSet):
    serializer_class = VeiculoSerializer
    queryset = Veiculo.objects.all()