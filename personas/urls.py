from django.urls import path
from .views import crearCliente, editarCliente, eliminarCliente, crearProveedor, editarProveedor, eliminarProveedor

urlpatterns = [
    path('cliente/nuevo/', crearCliente, name='cliente_create'),
    path('cliente/editar/<int:id_cliente>', editarCliente, name='cliente_edit'),
    path('cliente/eliminar/', eliminarCliente, name='cliente_delete'),
    path('proveedor/nuevo/', crearProveedor, name='proveedor_create'),
    path('proveedor/editar/<int:id_proveedor>', editarProveedor, name='proveedor_edit'),
    path('proveedor/eliminar/', eliminarProveedor, name='proveedor_delete'),
    
]