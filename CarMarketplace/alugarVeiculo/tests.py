from django.test import TestCase
from rest_framework.test import APIClient
from login.models import Cliente
from django.urls import reverse
from django.contrib.auth.models import User
from anunciarVeiculos.models import Veiculo, Modelo, Anuncio

class CriarAluguelTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.superuser = User.objects.create_superuser(username='admin@test.com',password='admin', first_name='Admin')
        self.user = User.objects.create_user(username='user@test.com', password='user', first_name='User')
        self.cliente = Cliente.objects.create(user=self.user, telefone='1234567890', cpf='12345678901', endereco='Test address')
        self.modelo = Modelo.objects.create(tipoCombustivel='gasolina', model='Modelo Teste', marca='Marca Teste', ano=2020, cambio=True, categoria='compacto', qtdPortas=4)
        self.veiculo = Veiculo.objects.create(placa='ABC1234', quilometragem='10000', status=False, modelo=self.modelo, dono=self.cliente, cor='Preto')
        self.anuncio = Anuncio.objects.create(pontos=10, img1='', img2='', descricao='Descricao Teste', veiculo=self.veiculo, destaque=False, preco=20000, servico=True)
        self.aluguel_data = {
            'email': 'user@test.com',
            'id': self.anuncio.id
        }

    def test_criar_aluguel(self):
        # Test for normal user
        self.client.login(username='user@test.com', password='user')
        response = self.client.post(reverse('Aluguel'), self.aluguel_data, format='json')
        print(response.json())  # Imprime a resposta no formato JSON
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'mensagem')