from rest_framework.routers import DefaultRouter
from .views import SolicitacaoViewSet, criarSolicitacao
from django.urls import path, include


router = DefaultRouter()
router.register(r'Solicitacao', SolicitacaoViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path ('criarSolicitacao/',criarSolicitacao,name='Solicitar')
]