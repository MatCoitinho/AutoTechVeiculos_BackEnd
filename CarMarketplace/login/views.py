from rest_framework import viewsets
from .models import Cliente
from django.contrib.auth.models import User
from .serializers import ClienteSerializer, UserSerializer




class ClienteViewSet(viewsets.ModelViewSet):
    serializer_class = ClienteSerializer
    queryset = Cliente.objects.all()

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()