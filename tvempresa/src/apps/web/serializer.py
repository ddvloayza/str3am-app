from rest_framework import serializers
from .models import Capitulos

class CapitulosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Capitulos
        fields = '__all__'
