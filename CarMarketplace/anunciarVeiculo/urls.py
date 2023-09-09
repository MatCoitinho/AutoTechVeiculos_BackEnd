from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import carroViewSet, VeiculoViewSet
#from django.contrib import admin


router = DefaultRouter()
router.register(r'Veiculo', VeiculoViewSet)
router.register(r'carro', carroViewSet)

urlpatterns = router.urls