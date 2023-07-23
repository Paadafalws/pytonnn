from rest_framework import viewsets, filters
from clientes.serializers import ClienteSerializer
from clientes.models import Cliente
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter


class ClientesViewSet(viewsets.ModelViewSet):
    """Listando clientes"""
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    filter_backends = [filters.OrderingFilter, SearchFilter, DjangoFilterBackend]  # Invertida a ordem dos filtros

    search_fields = ['nome', 'cpf']
    ordering_fields = ['nome', 'cpf']  
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
