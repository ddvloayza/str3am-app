from rest_framework import viewsets
from .models import Capitulos
from .serializer import CapitulosSerializer

class CapitulosViewSet(viewsets.ModelViewSet):
    queryset = Capitulos.objects.all()
    serializer_class = CapitulosSerializer