from rest_framework.routers import DefaultRouter
from .views import DesejoViewSet, adicionarDesejo
from django.urls import path, include


router = DefaultRouter()

router.register(r'Desejo', DesejoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('adicionarDesejo/',adicionarDesejo,name='AdicionarDesejo'),
    
]



