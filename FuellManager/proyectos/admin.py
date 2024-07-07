from django.contrib import admin
from .models import Planta, Producto, RegistroProduccion
from django.utils import timezone

# 
class RegistroProduccionAdmin(admin.ModelAdmin):
    list_display = ('codigo_combustible', 'litros_producidos', 'fecha_produccion', 'turno', 'operador', 'esta_eliminado', 'eliminado_por', 'eliminado_en')
    actions = ['marcar_como_eliminado']

    def marcar_como_eliminado(self, request, queryset):
        for registro in queryset:
            registro.esta_eliminado = True
            registro.eliminado_por = request.user
            registro.eliminado_en = timezone.now()
            registro.save()
        self.message_user(request, "Los registros seleccionados han sido marcados como eliminados.")
    
    marcar_como_eliminado.short_description = "Marcar los registros seleccionados como eliminados"

    def has_delete_permission(self, request, obj=None):
        # Permitir la eliminación lógica solo si el usuario pertenece al grupo de supervisores
        return request.user.groups.filter(name='Supervisores').exists()

admin.site.register(Planta)
admin.site.register(Producto)
admin.site.register(RegistroProduccion)