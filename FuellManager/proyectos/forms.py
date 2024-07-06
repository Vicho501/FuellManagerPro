from django import forms
from django.forms import ModelForm
from .models import RegistroProduccion, Producto, Planta, User

class RegistroProduccionForm(ModelForm):
    class Meta:
        model = RegistroProduccion
        fields = ['codigo_combustible', 'litros_producidos', 'fecha_produccion', 'turno', 'operador']

    def __init__(self, *args, **kwargs):
        super(RegistroProduccionForm, self).__init__(*args, **kwargs)
        self.fields['codigo_combustible'].queryset = Producto.objects.all()
        self.fields['operador'].queryset = User.objects.all()

    codigo_combustible = forms.ModelChoiceField(queryset=None, label='Código Combustible')
    litros_producidos = forms.FloatField(label='Litros Producidos')
    fecha_produccion = forms.DateField(label='Fecha de Producción', widget=forms.DateInput(attrs={'type': 'date'}))
    turno = forms.ChoiceField(label='Turno', choices=RegistroProduccion.TURNOS)
    operador = forms.ModelChoiceField(queryset=None, label='Operador')


class EditarProduccionForm(ModelForm):
    class Meta:
        model = RegistroProduccion
        fields = ['codigo_combustible', 'litros_producidos', 'fecha_produccion', 'turno', 'operador']

    def __init__(self, *args, **kwargs):
        super(RegistroProduccionForm, self).__init__(*args, **kwargs)
        self.fields['codigo_combustible'].queryset = Producto.objects.all()
        self.fields['operador'].queryset = User.objects.all()

    codigo_combustible = forms.ModelChoiceField(queryset=None, label='Código Combustible')
    litros_producidos = forms.FloatField(label='Litros Producidos')
    fecha_produccion = forms.DateField(label='Fecha de Producción', widget=forms.DateInput(attrs={'type': 'date'}))
    turno = forms.ChoiceField(label='Turno', choices=RegistroProduccion.TURNOS)
    operador = forms.ModelChoiceField(queryset=None, label='Operador')