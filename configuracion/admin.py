from django.contrib import admin
from .models import TContribuyente, TDocumento, Pais, Estado, Municipio

class TDocumentoAdmin(admin.ModelAdmin):
    list_display = ('id_tdoc', 'nombre', 'descripcion')
    search_fields = ('nombre',)
    ordering = ('id_tdoc',)

class TContribuyenteAdmin(admin.ModelAdmin):
    list_display = ('id_tcont', 'nombre', 'descripcion')
    search_fields = ('nombre',)
    ordering = ('id_tcont',)
    
class PaisAdmin(admin.ModelAdmin):
    list_display = ('id_pais', 'nombre')
    search_fields = ('nombre',)
    ordering = ('id_pais',)
    
class EstadoAdmin(admin.ModelAdmin):
    list_display = ('id_estado', 'nombre', 'id_pais')
    search_fields = ('nombre', 'id_pais')
    ordering = ('id_estado',)

class MunicipioAdmin(admin.ModelAdmin):
    list_display = ('id_municipio', 'nombre', 'id_estado')
    search_fields = ('nombre', 'id_estado')
    ordering = ('id_municipio',)
    

admin.site.register(TDocumento, TDocumentoAdmin)
admin.site.register(TContribuyente, TContribuyenteAdmin)
admin.site.register(Pais, PaisAdmin)
admin.site.register(Estado, EstadoAdmin)
admin.site.register(Municipio, MunicipioAdmin) 