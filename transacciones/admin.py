from django.contrib import admin
from .models import MedioPago, FormaPago, Cotizacion, Proforma, Inventario, DetallesCotizacion, DetallesProforma

class MedioPagoAdmin(admin.ModelAdmin):
    list_display = ('id_mpago', 'nombre', 'descripcion')
    search_fields = ('nombre', 'descripcion')
    ordering = ('id_mpago',)

class FormaPagoAdmin(admin.ModelAdmin):
    list_display = ('id_fpago', 'nombre', 'descripcion')
    search_fields = ('nombre', 'descripcion')
    ordering = ('id_fpago',)
    
class InventarioAdmin(admin.ModelAdmin):
    list_display = ('id_inventario', 'fecha', 'n_lote', 'id_proveedor')
    search_fields = ('id_proveedor', 'id_producto')
    ordering = ('id_inventario',)
    
class CotizacionAdmin(admin.ModelAdmin):
    list_display = ('id_cotizacion', 'id_trabajador', 'fecha_emision', 'fecha_vencimiento', 'estado')
    search_fields = ('estado', 'id_trabajador', 'id_cliente')
    ordering = ('id_cotizacion',)
    
class DetallesCotizacionAdmin(admin.ModelAdmin):
    list_display = ('id_dcotizacion','id_cotizacion')
    search_fields = ('id_producto', 'id_cotizacion')
    ordering = ('id_dcotizacion',)
    
class ProFormaAdmin(admin.ModelAdmin):
    list_display = ('id_proforma', 'id_trabajador', 'fecha_emision', 'fecha_vencimiento', 'estado')
    search_fields = ('estado', 'id_trabajador', 'id_cliente')
    ordering = ('id_proforma',)
    
class DetallesProFormaAdmin(admin.ModelAdmin):
    list_display = ('id_dproforma','id_proforma')
    search_fields = ('id_producto', 'id_proforma')
    ordering = ('id_dproforma',)
    

    
    

admin.site.register(MedioPago, MedioPagoAdmin)
admin.site.register(FormaPago, FormaPagoAdmin)
admin.site.register(Inventario, InventarioAdmin)
admin.site.register(Cotizacion, CotizacionAdmin)
admin.site.register(DetallesCotizacion, DetallesCotizacionAdmin)
admin.site.register(Proforma, ProFormaAdmin)
admin.site.register(DetallesProforma, DetallesProFormaAdmin)