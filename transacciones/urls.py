from django.urls import path
from .views import crearMedioPago, editarMedioPago, eliminarMedioPago, crearFormaPago, editarFormaPago, eliminarFormaPago, cotizacionDetalles, buscar_productos, get_producto_info, cotizacion_list, procesar_seleccion, buscar_cliente
from . import views

urlpatterns = [
    path('mediopago/nuevo/', crearMedioPago, name='mediopago_create'),
    path('mediopago/editar/<int:id_mpago>/', editarMedioPago, name='mediopago_edit'),
    path('mediopago/eliminar/<int:id_mpago>/', eliminarMedioPago, name='mediopago_delete'),
    path('formapago/nuevo/', crearFormaPago, name='formapago_create'),
    path('formapago/editar/<int:id_fpago>/', editarFormaPago, name='formapago_edit'),
    path('formapago/eliminar/<int:id_fpago>/', eliminarFormaPago, name='formapago_delete'),
    path('cotizacion/nuevo/', cotizacionDetalles, name='cotizacion_create'),
    path('cotizacion/listado/', cotizacion_list, name='cotizacion_list'),
    path('buscar_cliente/', buscar_cliente, name='buscar_cliente'),
    path('buscar_productos/', views.buscar_productos, name='buscar_productos'),
    path('select-products/', views.select_products, name='select_products'),
    path('get-producto-info/', get_producto_info, name='get_producto_info'),
    path('procesar_seleccion/', views.procesar_seleccion, name='procesar_seleccion'),
]
