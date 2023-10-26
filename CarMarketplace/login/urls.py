from rest_framework.routers import DefaultRouter

from .views import ClienteViewSet, Cadastrar

from django.urls import path, include


router = DefaultRouter()

router.register(r'Cliente', ClienteViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('cadastrar/',Cadastrar,name='Cadastrar')
]