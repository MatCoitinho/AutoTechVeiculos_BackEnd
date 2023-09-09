# from django.shortcuts import render
from rest_framework import viewsets
from .models import carro, Veiculo
from .serializers import carroSerializer, VeiculoSerializer


class carroViewSet(viewsets.ModelViewSet):
    serializer_class = carroSerializer
    queryset = carro.objects.all()

class VeiculoViewSet(viewsets.ModelViewSet):
    serializer_class = VeiculoSerializer
    queryset = Veiculo.objects.all()