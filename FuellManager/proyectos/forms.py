from django import forms
from .models import RegistroProduccion

class RegistroProduccionFrom(forms,ModelFrom):
    class Meta:
        model= RegistroProduccion
        field= ['codigo_combustible','litros_producidos', 'fecha_procuccion','turno']
        widgets={
            'fecha_produccion':froms.DateInput(attrs={'type':'date'}),
        }