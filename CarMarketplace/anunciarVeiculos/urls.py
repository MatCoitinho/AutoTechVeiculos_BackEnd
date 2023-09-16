from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ModeloViewSet, VeiculoViewSet, AnuncioViewSet
#from django.contrib import admin


router = DefaultRouter()
router.register(r'Modelo', VeiculoViewSet)
router.register(r'Veiculo', ModeloViewSet)
router.register(r'Anuncio', AnuncioViewSet)

urlpatterns = router.urls