from django.contrib import admin

from .models import Paises, Estados, Cidades


@admin.register(Paises)
class PaisesAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'pais', 'sigla', 'ddi', 'dataCad', 'dataUpdate' )


@admin.register(Estados)
class EstadosAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'estado', 'uf', 'pais', 'dataCad', 'dataUpdate')


@admin.register(Cidades)
class CidadesAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'cidade', 'ddd', 'estado', 'dataCad', 'dataUpdate')