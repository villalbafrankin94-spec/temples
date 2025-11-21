from rest_framework import serializers
from .models import Repartidor

class RepartidorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Repartidor
        fields = '__all__'
