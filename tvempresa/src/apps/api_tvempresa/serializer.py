from rest_framework import serializers
from apps.web.models import Capitulos, Programa, Principal
from django.contrib.sites.shortcuts import get_current_site

class CapitulosSerializer(serializers.ModelSerializer):

    class Meta:
        model = Capitulos
        fields = '__all__'


class ProgramasSerializer(serializers.ModelSerializer):
    programa = CapitulosSerializer(many=True)
    class Meta:
        model = Programa
        fields = ('nombre', 'imagen_programa', 'programa')


class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Principal
        fields = '__all__'
