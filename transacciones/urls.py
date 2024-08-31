from django.urls import path
from .views import crearMedioPago, editarMedioPago, eliminarMedioPago

urlpatterns = [
    path('mediopago/nuevo/', crearMedioPago, name='mediopago_create'),
    path('mediopago/editar/<int:id_mpago>/', editarMedioPago, name='mediopago_edit'),
    path('mediopago/eliminar/<int:id_mpago>/', eliminarMedioPago, name='mediopago_delete'),
]
