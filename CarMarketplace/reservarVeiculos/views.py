from django.shortcuts import render
from .models import Reserva
from .serializers import ReservaSerializer
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

class ReservaViewSet(viewsets.ModelViewSet):
    serializer_class = ReservaSerializer
    queryset = Reserva.objects.all()
    permission_classes = [AllowAny]
