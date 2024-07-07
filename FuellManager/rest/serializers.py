from rest_framework import serializers
from proyectos.models import RegistroProduccion

class ProduccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroProduccion
        fields = ('codigo_combustible', 'litros_producidos','fecha_produccion', 'turno', 'hora_registro', 'operador')
        read_only_fields = ('hora_registro', )