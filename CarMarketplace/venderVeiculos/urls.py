from rest_framework.routers import DefaultRouter
from .views import VendaViewSet, criar_venda
from django.urls import path, include


router = DefaultRouter()
router.register(r'Venda', VendaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('criarVenda/',criar_venda,name='Vender')
]