from rest_framework.routers import DefaultRouter
from .views import SolicitacaoViewSet
from django.urls import path, include


router = DefaultRouter()
router.register(r'Solicitacao', SolicitacaoViewSet)


urlpatterns = [
    path('', include(router.urls)),
]