from django.shortcuts import render
from rest_framework import viewsets, permissions
from proyectos.models import RegistroProduccion, Planta, Producto
from .serializers import ProduccionSerializer, PlantaSerializer, ProductoSerializer
from proyectos.models import Planta, Producto, RegistroProduccion
from django_filters.rest_framework import DjangoFilterBackend
from proyectos.filters import ProduccionFilter
from django.db.models import Sum
from rest_framework.response import Response

class PlantaViewSet(viewsets.ModelViewSet):
    queryset = Planta.objects.all()
    serializer_class = PlantaSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class ProduccionViewSet(viewsets.ModelViewSet):
    queryset = RegistroProduccion.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProduccionSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_class = ProduccionFilter

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)

        # Calcular la suma de litros producidos para los registros filtrados
        total_producido = queryset.aggregate(Sum('litros_producidos'))['litros_producidos__sum']

        # Agregar el total_producido al contexto de respuesta
        data = serializer.data
        data.append({'total_producido': total_producido})

        return Response(data)