from rest_framework import serializers
from proyectos.models import Planta, Producto, RegistroProduccion

class PlantaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planta
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class ProduccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroProduccion
        fields = ('codigo_combustible', 'litros_producidos','fecha_produccion', 'turno', 'hora_registro', 'operador')
        read_only_fields = ('hora_registro', )