from django.shortcuts import render
from rest_framework import viewsets, permissions
from proyectos.models import RegistroProduccion
from .serializers import ProduccionSerializer

class ProduccionViewSet(viewsets.ModelViewSet):
    queryset = RegistroProduccion.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProduccionSerializer