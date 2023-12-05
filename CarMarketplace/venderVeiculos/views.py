from django.shortcuts import render
from .serializers import VendaSerializer
from .models import Venda
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

class VendaViewSet(viewsets.ModelViewSet):
    serializer_class = VendaSerializer
    queryset = Venda.objects.all()
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['veiculo__modelo__model','cpf_comprador','nome_comprador']