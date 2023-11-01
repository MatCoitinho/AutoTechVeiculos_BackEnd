from rest_framework.routers import DefaultRouter

from .views import ClienteViewSet, Cadastrar, Logar, retrieveUserCliente, Atualizar

from django.urls import path, include


router = DefaultRouter()

router.register(r'Cliente', ClienteViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('cadastrar/',Cadastrar,name='Cadastrar'),
    path('logar/',Logar,name='Logar'),
    path('retrieve/',retrieveUserCliente, name='Retrieve'),
    path('atualizar/',Atualizar,name='Atualizar'),
]