from django.contrib import admin
from .models import Planta, Producto, RegistroProduccion
from django.utils import timezone

# Register your models here.


admin.site.register(Planta)
admin.site.register(Producto)
admin.site.register(RegistroProduccion)