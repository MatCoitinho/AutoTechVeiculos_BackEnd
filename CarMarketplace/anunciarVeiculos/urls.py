from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ModeloViewSet, VeiculoViewSet, AnuncioViewSet, criarVeiculo, criarAnuncio
from django.contrib import admin


router = DefaultRouter()
router.register(r'Modelo', ModeloViewSet)
router.register(r'Veiculo', VeiculoViewSet)
router.register(r'Anuncio', AnuncioViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('criarVeiculo/',criarVeiculo,name='criar_veiculo'),
    path('criarAnuncio/',criarAnuncio,name='criar_anuncio'),
]