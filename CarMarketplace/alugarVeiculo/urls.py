from rest_framework.routers import DefaultRouter
from .views import AlugarViewSet, criarAluguel
from django.urls import path, include

router = DefaultRouter()

router.register(r'Alugar',AlugarViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('criarAluguel/',criarAluguel,name='Aluguel')
]