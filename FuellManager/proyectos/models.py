from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#la siguiente clase es para el nombre de la pnata y su codigo
class Planta(models.model):
    codigo= models.CharField(max_length=3, unique=True)
    nombre= models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

#esta clase es para la produccion de la planta
class Produto(models.Model):
    codigo= models.CharField(max_length=3, unique=True)
    nombre= models.CharField(max_length=100)
    planta= models.Forighkey(Planta, on_delete=models.CASCADE)#crea una clave foranea

    def __str__ (self):
        return self.nombre

#clase que reguistra la produccion
class RegistroProduccion(models.Model):
    TURNOS=[
        ('AM','MAÑANA'),
        ('PM','TARDE'),
        ('MM','NOCHE'),
    ]

    codigo_combustible= models.Forighkey(Produto, on_delete=models.CASCADE)
    litros_producidos= models.FloatField()
    fecha_produccion= models.FloatField()
    turno= models.CharField(max_length=2, choices=TURNOS)
    hora_registro= models.DataTimeField(auto_now_add=True)
    operador=models.Forighkey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.codigo_combustible}-{self.fecha_produccion}-{self.turno}"
