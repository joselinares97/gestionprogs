from django.contrib import admin
from .models import Cliente, Proveedor

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id_cliente', 'nombre', 'apellido', 'n_doccl', 'email', 'telefono', 'id_municipio')
    search_fields = ('nombre', 'apellido', 'n_doccl', 'email', 'telefono')
    list_filter = ('id_tdoc', 'id_tcont', 'id_municipio')

class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('id_proveedor', 'nombre', 'num_docpro', 'email', 'telefono', 'id_municipio')
    search_fields = ('nombre', 'num_docpro', 'email', 'telefono')
    list_filter = ('id_tdoc', 'id_tcont', 'id_municipio')

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Proveedor, ProveedorAdmin)
