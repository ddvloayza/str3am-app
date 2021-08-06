from apps.web.models import (Capitulos)

from .serializer import CapitulosSerializer
from rest_framework import generics


class CapitulosList(generics.ListCreateAPIView):
    queryset = Capitulos.objects.all()
    serializer_class = CapitulosSerializer


class CapitulosDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Capitulos.objects.all()
    serializer_class = CapitulosSerializer