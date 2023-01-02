from django.contrib import admin
from .models import Reclamo, Respuesta, Categoria

class RespuestaInline(admin.TabularInline):
    model = Respuesta
    extra = 2

class ReclamoAdmin(admin.ModelAdmin):
    list_display = ['tiket','categoria', 'fecha_creada', 'estado', 'fecha_modificada']

    inlines = [RespuestaInline]

admin.site.register(Reclamo, ReclamoAdmin)
admin.site.register(Respuesta)
admin.site.register(Categoria)
