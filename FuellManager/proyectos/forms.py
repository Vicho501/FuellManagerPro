from django import forms
from django.forms import ModelForm
from .models import RegistroProduccion

class RegistroProduccionForm(ModelForm):
    class Meta:
        model = RegistroProduccion
        fields = ['codigo_combustible', 'litros_producidos', 'fecha_produccion', 'turno'] 
        widgets = {
            'fecha_produccion': forms.DateInput(attrs={'type': 'date'}),
        }