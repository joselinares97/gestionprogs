from django.urls import path
from .views import crearCategoria, editarCategoria, eliminarCategoria, crearProducto, editarProducto, eliminarProducto

urlpatterns = [
    path('categoria/nuevo/', crearCategoria, name='categoria_create'),
    path('categoria/editar/<int:id_cat>', editarCategoria, name='categoria_edit'),
    path('categoria/eliminar/<int:id_cat>/', eliminarCategoria, name='categoria_delete'),
    path('producto/nuevo/', crearProducto, name='producto_create'),
    path('producto/editar/<int:id_producto>', editarProducto, name='producto_edit'),
    path('producto/eliminar/<int:id_producto>/', eliminarProducto, name='producto_delete'),
]