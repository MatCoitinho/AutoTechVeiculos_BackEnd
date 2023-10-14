from rest_framework.routers import DefaultRouter
from .views import ReservaViewSet
from django.urls import path, include

router = DefaultRouter()

router.register(r'Reserva', ReservaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]