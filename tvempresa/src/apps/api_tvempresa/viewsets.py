from rest_framework import viewsets
from apps.web.models import Capitulos, Programa, Principal
from .serializer import CapitulosSerializer, ProgramasSerializer, HomeSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from collections import OrderedDict
from rest_framework import filters

class LargeResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('count', self.page.paginator.count),
            ('page', self.page.number),
            ('num_page', self.page.paginator.num_pages),
            ('results', data)
        ]))


class CapitulosViewSet(viewsets.ModelViewSet):
    queryset = Capitulos.objects.filter(programa__active=True)
    serializer_class = CapitulosSerializer
    pagination_class = LargeResultsSetPagination


class ProgramasViewSet(viewsets.ModelViewSet):
    queryset = Programa.objects.filter(active=True)
    serializer_class = ProgramasSerializer
    pagination_class = LargeResultsSetPagination


class SearchCapituloList(viewsets.ModelViewSet):
        queryset = Capitulos.objects.filter(programa__active=True)
        serializer_class = CapitulosSerializer
        filter_backends = [filters.SearchFilter]
        pagination_class = LargeResultsSetPagination
        search_fields = ['programa__nombre', 'titulo']


class HomeViewSet(viewsets.ModelViewSet):
    queryset = Principal.objects.all()
    serializer_class = HomeSerializer
