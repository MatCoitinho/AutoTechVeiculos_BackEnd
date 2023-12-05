from .models import Desejo
from rest_framework import serializers

class DesejoSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Desejo
        fields = '__all__'