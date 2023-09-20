from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from .models import Modelo, Veiculo, Cliente
from django.contrib.auth.models import User


class ModeloTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_modelo(self):
        data = {
            "tipoCombustivel": "gasolina",
            "model": "Modelo Teste",
            "marca": "Marca Teste",
            "ano": 2023,
            "cambio": True,
            "categoria": "compacto",
            "qtdPortas": 4
        }
        response = self.client.post(reverse('modelo-list'), data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Modelo.objects.count(), 1)
        self.assertEqual(Modelo.objects.get().model, 'Modelo Teste')


class VeiculoTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='user_teste',
            password='senha_teste'
        )
        self.cliente = Cliente.objects.create(
            cpf="12345678901",
            telefone="11987654321",
            endereco="Rua Teste, 123",
            user=self.user
        )
        self.modelo = Modelo.objects.create(
            tipoCombustivel=Modelo.TipoCombustivel.gasolina,
            model='Modelo Teste',
            marca='Marca Teste',
            ano=2023,
            cambio=True,
            categoria=Modelo.CategoriaCarro.compacto,
            qtdPortas=4
        )

    def test_create_veiculo(self):
        data = {
            "placa": "ABC1234",
            "quilometragem": "10000",
            "status": True,
            "preco": 50000,
            "veiculo": self.modelo.id,
            "servico": False,
            "dono": self.cliente.id,
            "cor": "Azul"
        }
        response = self.client.post(reverse('veiculo-list'), data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Veiculo.objects.count(), 1)
        self.assertEqual(Veiculo.objects.get().placa, 'ABC1234')