from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APIClient
from .models import Cliente


# class RetrieveUserClienteTest(TestCase):
#     def setUp(self):
#         self.client = APIClient()
#         self.superuser = User.objects.create_superuser(username='admin@test.com',password='admin', first_name='Admin')
#         self.user = User.objects.create_user(username='user@test.com', password='user', first_name='User')
#         self.cliente = Cliente.objects.create(user=self.user, telefone='1234567890', cpf='12345678901', endereco='Test address')

#     def test_retrieve_user_cliente(self):
#         # Test for superuser
#         # response = self.client.post(reverse('Retrieve'), {'email': 'admin@test.com'}, format='json')
#         # print(response.json())  # Imprime a resposta no formato JSON
#         # self.assertEqual(response.status_code, 200)
#         # self.assertContains(response, 'id')
#         # self.assertContains(response, 'name')
#         # self.assertContains(response, 'email')
#         # self.assertContains(response, 'phone')
#         # self.assertContains(response, 'cpf')
#         # self.assertContains(response, 'address')
#         # self.assertContains(response, 'is_superuser')

#         # Test for normal user
#         # response = self.client.post(reverse('Retrieve'), {'email': 'user@test.com'}, format='json')
#         # print(response.json())  # Imprime a resposta no formato JSON
#         # self.assertEqual(response.status_code, 200)
#         # self.assertContains(response, 'id')
#         # self.assertContains(response, 'name')
#         # self.assertContains(response, 'email')
#         # self.assertContains(response, 'phone')
#         # self.assertContains(response, 'cpf')
#         # self.assertContains(response, 'address')
#         # self.assertContains(response, 'is_superuser')

#         # Test for invalid email
#         response = self.client.post(reverse('Retrieve'), {'email': 'invalid@test.com'}, format='json')
#         print(response.json())  # Imprime a resposta no formato JSON
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, 'erro')

        # Test for invalid method
        # response = self.client.post(reverse('Retrieve'), {'email': 'admin@test.com'}, format='json')
        # print(response.json())  # Imprime a resposta no formato JSON
        # self.assertEqual(response.status_code, 200)
        # self.assertContains(response, 'erro')

# class LogarTest(TestCase):
#     def setUp(self):
#         self.client = APIClient()
#         self.user = User.objects.create_user(username='mhcl0303@gmail.com', password='testpass', first_name = 'Coito')
#         self.cliente = Cliente.objects.create(user=self.user, telefone='123456789', cpf='12345678901', endereco='Test address')

#     def test_logar(self):
#         response = self.client.post(reverse('Logar'), {'email': 'mhcl0303@gmail.com', 'password': 'testpass'}, format='json')
#         print(response.json())  # Imprime a resposta no formato JSON
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, 'refresh')
#         self.assertContains(response, 'access')
#         self.assertContains(response, 'user')


# class CadastrarViewTestCase(TestCase):
#     def test_cadastrar_usuario_e_cliente(self):
#         # Define os dados de teste para a criação do usuário e cliente
#         data = {
#             "username": "Coito",
#             "senha": "senha123",
#             "primeiroNome": "Matheus",
#             "email": "novo@cliente.com",
#             "ultimoNome": "Coitinho",
#             "CPF" : "20143298644",
#             "endereco" : "rua 1, 872",
#             "telefone" : "66987124566"
#         }

#         # Faz uma solicitação POST à view 'cadastrar' com os dados de teste
#         response = self.client.post(reverse('Cadastrar'), json.dumps(data), content_type='application/json')

#         # Verifica se a resposta foi bem-sucedida (status HTTP 200)
#         self.assertEqual(response.status_code, 200)

#         # Verifica se o usuário foi criado no banco de dados
#         self.assertTrue(User.objects.filter(username='novo@cliente.com').exists())

#         # Verifica o conteúdo da resposta JSON
#         self.assertJSONEqual(str(response.content, encoding='utf8'), {'mensagem': 'Usuario Cadastrado com Sucesso'})
