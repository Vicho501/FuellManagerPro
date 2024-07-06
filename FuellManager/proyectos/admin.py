from django.contrib import admin
from .models import Planta, Produto, RegistroProduccion
from django.utils import timezone

# Register your models here.


admin.site.register(Planta)
admin.site.register(Produto)
admin.site.register(RegistroProduccion)