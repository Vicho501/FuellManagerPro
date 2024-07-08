from django.shortcuts import render
from rest_framework import viewsets, permissions
from proyectos.models import RegistroProduccion, Planta, Producto
from .serializers import ProduccionSerializer, PlantaSerializer, ProductoSerializer
from proyectos.models import Planta, Producto, RegistroProduccion
from django_filters.rest_framework import DjangoFilterBackend


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
    filterset_fields = {
        'codigo_combustible__nombre': ['exact'],
        'codigo_combustible__planta__nombre': ['exact'],
        'fecha_produccion': ['year', 'month'],
    }