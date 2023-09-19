from django.contrib.auth.models import User
from .models import Cliente
from django.test import TestCase
from django.urls import reverse
import json

class CadastrarViewTestCase(TestCase):
    def test_cadastrar_usuario_e_cliente(self):
        # Define os dados de teste para a criação do usuário e cliente
        data = {
            "username": "Coito",
            "senha": "senha123",
            "primeiroNome": "Matheus",
            "email": "novo@cliente.com",
            "ultimoNome": "Coitinho",
            "CPF" : "20143298644",
            "endereco" : "rua 1, 872",
            "telefone" : "66987124566"
        }

        # Faz uma solicitação POST à view 'cadastrar' com os dados de teste
        response = self.client.post(reverse('Cadastrar'), json.dumps(data), content_type='application/json')

        # Verifica se a resposta foi bem-sucedida (status HTTP 200)
        self.assertEqual(response.status_code, 200)

        # Verifica se o usuário foi criado no banco de dados
        self.assertTrue(User.objects.filter(username='Coito').exists())

        # Verifica se outros dados do cliente foram criados no banco de dados
        # Adicione as verificações necessárias aqui

        # Verifica o conteúdo da resposta JSON
        self.assertJSONEqual(str(response.content, encoding='utf8'), {'mensagem': 'Usuario Cadastrado com Sucesso'})
