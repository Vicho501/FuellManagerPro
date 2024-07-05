from django.contrib import admin
from .models import Planta, Produto, RegistroProduccion
from django.utils import timezone

# Register your models here.
class RegistroProduccionAdmin(admin.ModelAdmin):
    list_display=('producto', 'litros', 'fecha_producción', 'cambio', 'operador', 'está_eliminado', 'eliminado_por', 'eliminado_at')
    actions=['marcar_eliminado']

    def marcar_eliminado(self, request, queryset):
        for record in queryset:
            record.está_eliminado=True
            record.eliminado_por=request.user
            record.eliminado_at=timezone.now()
            record.save()
            self.massage_user(request"Los registros seleccionados se han marcado como eliminados.")
    marcar_eliminado.short_description="Marcar registros seleccionados como eliminados"

admin.site.register(Planta)
admin.site.register(Produto)
admin.site.register(RegistroProduccion RegistroProduccionAdmin)