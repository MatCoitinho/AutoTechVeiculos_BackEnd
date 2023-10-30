from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from .models import Modelo, Veiculo, Cliente, Anuncio
from django.contrib.auth.models import User
import json
from django.test.utils import override_settings
from django.core import serializers


# class ModeloTestCase(TestCase):
#     def setUp(self):
#         self.client = APIClient()

#     def test_create_modelo(self):
#         data = {
#             "tipoCombustivel": "gasolina",
#             "model": "Modelo Teste",
#             "marca": "Marca Teste",
#             "ano": 2023,
#             "cambio": True,
#             "categoria": "compacto",
#             "qtdPortas": 4
#         }
#         response = self.client.post(reverse('modelo-list'), data, format='json')
#         self.assertEqual(response.status_code, 201)
#         self.assertEqual(Modelo.objects.count(), 1)
#         self.assertEqual(Modelo.objects.get().model, 'Modelo Teste')


# class VeiculoTestCase(TestCase):
#     def setUp(self):
#         self.client = APIClient()
#         self.user = User.objects.create_user(
#             username='user_teste',
#             password='senha_teste'
#         )
#         self.cliente = Cliente.objects.create(
#             cpf="12345678901",
#             telefone="11987654321",
#             endereco="Rua Teste, 123",
#             user=self.user
#         )
#         self.modelo = Modelo.objects.create(
#             tipoCombustivel=Modelo.TipoCombustivel.gasolina,
#             model='Modelo Teste',
#             marca='Marca Teste',
#             ano=2023,
#             cambio=True,
#             categoria=Modelo.CategoriaCarro.compacto,
#             qtdPortas=4
#         )

#     def test_create_veiculo(self):
#         self.client = APIClient()
#         self.user = User.objects.create_user(
#             username='user_teste',
#             password='senha_teste'
#         )
#         self.cliente = Cliente.objects.create(
#             cpf="10104136944",
#             telefone="11987654321",
#             endereco="Rua Teste, 123",
#             user=self.user
#         )
#         self.modelo = Modelo.objects.create(
#             tipoCombustivel=Modelo.TipoCombustivel.gasolina,
#             model='Camaro',
#             marca='Chevrolet',
#             ano=2020,
#             cambio=True,
#             categoria=Modelo.CategoriaCarro.esportivo,
#             qtdPortas=2
#         )
#         data = {
#             "placa": "ABC1234",
#             "quilometragem": "10000",
#             "status": True,
#             "preco": 50000,
#             "veiculo": self.modelo.id,
#             "servico": False,
#             "dono": self.cliente.id,
#             "cor": "Azul"
#         }
#         response = self.client.post(reverse('veiculo-list'), data, format='json')
#         self.assertEqual(response.status_code, 201)
#         self.assertEqual(Veiculo.objects.count(), 1)
#         self.assertEqual(Veiculo.objects.get().placa, 'ABC1234')

class criarVeiculoViewTestCase(TestCase):
    def test_criarVeiculo(self):
        self.user = User.objects.create_user(
             username='MatheusCoito',
             password='sakuta03'
        )
        self.cliente = Cliente.objects.create(
             cpf="10104136944",
             telefone="11987654321",
             endereco="Rua Teste, 123",
             user=self.user
        )

        self.modelo = Modelo.objects.create(
            tipoCombustivel=Modelo.TipoCombustivel.gasolina,
            model='Camaro',
            marca='Chevrolet',
            ano=2020,
            cambio=True,
            categoria=Modelo.CategoriaCarro.esportivo,
            qtdPortas=2
        )

        data = {
            "placa": "PQA9812",
            "quilometragem": "0",
            "status": False,
            "cor": "Preto",
            "modelo": "Camaro",
            "ano" : "2020",
            "dono" : "10104136944",
        
        }

        # Faz uma solicitação POST à view 'criarVeiculo' com os dados de teste
        response = self.client.post(reverse('criar_veiculo'), json.dumps(data), content_type='application/json')

        # Verifica se a resposta foi bem-sucedida (status HTTP 200)
        self.assertEqual(response.status_code, 200)

        # Verifica se o usuário foi criado no banco de dados
        self.assertTrue(Veiculo.objects.filter(placa='PQA9812').exists())

        # Verifica o conteúdo da resposta JSON
        self.assertJSONEqual(str(response.content, encoding='utf8'), {'mensagem': 'Veiculo criado com sucesso'})

# class criarAnuncioViewTestCase(TestCase):
#     def test_criarAnuncio(self):
#         self.user = User.objects.create_user(
#              username='MatheusCoito',
#              password='sakuta03'
#         )

#         self.cliente = Cliente.objects.create(
#              cpf="10104136944",
#              telefone="11987654321",
#              endereco="Rua Teste, 123",
#              user=self.user
#         )

#         self.modelo = Modelo.objects.create(
#             tipoCombustivel=Modelo.TipoCombustivel.gasolina,
#             model='Camaro',
#             marca='Chevrolet',
#             ano=2020,
#             cambio=True,
#             categoria=Modelo.CategoriaCarro.esportivo,
#             qtdPortas=2
#         )

#         self.veiculo = Veiculo.objects.create(
#             placa = 'ANO4185',
#             quilometragem = 0,
#             status = True,
#             modelo = self.modelo,
#             dono = self.cliente,
#             cor = 'Preto'
#         )

#         data = {
#             # "pontos": "100",
#             # "img1": "dasdada",
#             # "img2": "sdadsadasd",
#             # "descricao": "nada de mais",
#             # "placa": "ANO4185",
#             # "destaque" : True,
#             # "preco" : "100000",
#             # "servico": False
#         'pontos': "0", 
#         'img1': 'https://firebasestorage.googleapis.com/v0/b/endless-sol-403405.appspot.com/o/images%2FIMG_20231011_202609.jpg?alt=media&token=29c1d10b-2470-4605-b1e6-46ef2d8850f7', 
#         'img2': 'https://firebasestorage.googleapis.com/v0/b/endless-sol-403405.appspot.com/o/images%2FIMG_20231011_202609.jpg?alt=media&token=0f915385-9390-4885-aa3f-97433020d077',
#         'descricao': '1',
#         'placa': 'ANO4185', 
#         'destaque': True,
#         'preco': "1",
#         'servico': True

#         }

#         # Faz uma solicitação POST à view 'criarVeiculo' com os dados de teste
#         response = self.client.post(reverse('criar_anuncio'), json.dumps(data), content_type='application/json')

#         # Verifica se a resposta foi bem-sucedida (status HTTP 200)
#         self.assertEqual(response.status_code, 200)

#         veic = Veiculo.objects.get(placa = 'ANO4185')

#         # Verifica se o usuário foi criado no banco de dados
#         self.assertTrue(Anuncio.objects.filter(veiculo=veic ,servico = True).exists())

#         # Verifica o conteúdo da resposta JSON
#         self.assertJSONEqual(str(response.content, encoding='utf8'), {'mensagem': 'Anuncio criado com sucesso'})
