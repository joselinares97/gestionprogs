from django.contrib import admin
from .models import Categoria, Productos

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id_cat', 'nombre', 'descripcion')
    search_fields = ('nombre', 'descripcion')
    ordering = ('id_cat',)
    
class ProductosAdmin(admin.ModelAdmin):
    list_display = ('id_producto', 'cod_producto', 'nombre', 'marca', 'id_cat')
    search_fields = ('nombre', 'cod_producto', 'marca', 'id_cat')
    ordering = ('id_producto', 'cod_producto', 'id_cat',)
    
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Productos, ProductosAdmin)