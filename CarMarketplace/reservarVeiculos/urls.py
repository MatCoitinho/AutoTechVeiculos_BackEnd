from rest_framework.routers import DefaultRouter
from .views import ReservaViewSet, criarReserva
from django.urls import path, include

router = DefaultRouter()

router.register(r'Reserva', ReservaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('criarReserva/',criarReserva,name='Reservar')
]