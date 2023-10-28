from django.shortcuts import render
from .models import Alugar
from .serializers import AlugarSerializer
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend

class AlugarViewSet(viewsets.ModelViewSet):
    serializer_class = AlugarSerializer
    queryset = Alugar.objects.all()
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['veiculo__modelo__model','cliente__cpf']