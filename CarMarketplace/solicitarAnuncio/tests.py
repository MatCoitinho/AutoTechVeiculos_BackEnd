from django.test import TestCase
from rest_framework.test import APIClient
from login.models import Cliente
from django.urls import reverse
from django.contrib.auth.models import User


class CriarSolicitacaoTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.superuser = User.objects.create_superuser(username='admin@test.com',password='admin', first_name='Admin')
        self.user = User.objects.create_user(username='user@test.com', password='user', first_name='User')
        self.cliente = Cliente.objects.create(user=self.user, telefone='1234567890', cpf='12345678901', endereco='Test address')
        self.solicitacao_data = {
            'solicitante': 'user@test.com',
            'marca': 'Marca Teste',
            'modelo': 'Modelo Teste',
            'ano': '2020',
            'quilometragem': '10000',
            'cambio': 'Manual',
            'servico': 'Servico Teste',
            'combustivel': 'Gasolina'
        }

    def test_criar_solicitacao(self):
        # Test for normal user
        self.client.login(username='user@test.com', password='user')
        response = self.client.post(reverse('Solicitar'), self.solicitacao_data, format='json')
        print(response.json())  # Imprime a resposta no formato JSON
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'mensagem')

        # Test for missing fields
        # del self.solicitacao_data['marca']
        # response = self.client.post(reverse('Solicitar'), self.solicitacao_data, format='json')
        # print(response.json())  # Imprime a resposta no formato JSON
        # self.assertEqual(response.status_code, 400)
        # self.assertContains(response, 'erro')

        # Test for wrong method
        # response = self.client.get(reverse('criarSolicitacao'))
        # print(response.json())  # Imprime a resposta no formato JSON
        # self.assertEqual(response.status_code, 405)
        # self.assertContains(response, 'erro')
# Create your tests here.
