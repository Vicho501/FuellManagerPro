from django.shortcuts import render
from rest_framework import viewsets, permissions
from proyectos.models import RegistroProduccion
from .serializers import ProduccionSerializer, PlantaSerializer, ProductoSerializer
from proyectos.models import Planta, Producto, RegistroProduccion

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

    filterset_fields = {
        
    }