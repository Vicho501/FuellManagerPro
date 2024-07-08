import django_filters
from django.db.models import Sum
from proyectos.models import RegistroProduccion

class ProduccionFilter(django_filters.FilterSet):
    nombre_combustible = django_filters.CharFilter(field_name='codigo_combustible__nombre', label='Nombre combustible')
    nombre_planta = django_filters.CharFilter(field_name='codigo_combustible__planta__nombre', label='Nombre de la Planta')
    ano_produccion = django_filters.NumberFilter(field_name='fecha_produccion__year', label='Año de produccion')
    mes_produccion = django_filters.NumberFilter(field_name='fecha_produccion__month', label='Mes de Produccion')
    total_producido = django_filters.Filter(method='filter_total_producido', label='Total Producido')


    class Meta:
        model = RegistroProduccion
        fields = ['nombre_combustible', 'nombre_planta', 'ano_produccion', 'mes_produccion', 'total_producido']

    def filter_total_producido(self, queryset, name, value):
        return queryset.annotate(total_producido=Sum('litros_producidos'))