from django.urls import path
from .views import crearTContribuyente, crearTDocumento, crearPais, crearEstado, crearMunicipio, editarTContribuyente, editarTDocumento, editarPais, editarEstado, editarMunicipio, eliminarTContribuyente, eliminarTDocumento

urlpatterns = [
    path('tcontribuyente/nuevo/', crearTContribuyente, name='tcontribuyente_create'),
    path('tcontribuyente/editar/<int:id_tcont>', editarTContribuyente, name='tcontribuyente_edit'),
    path('tcontribuyente/eliminar/', eliminarTContribuyente, name='tcontribuyente_delete'),
    path('tdocumento/nuevo/', crearTDocumento, name='tdocumento_create'),
    path('tdocumento/editar/<int:id_tdoc>/', editarTDocumento, name='tdocumento_edit'),
    path('tdocumento/eliminar/', eliminarTDocumento, name='tdocumento_delete'),
    path('pais/nuevo/', crearPais, name='pais_create'),
    path('pais/editar/<int:id_pais>/', editarPais, name='pais_edit'),
    path('estado/nuevo/', crearEstado, name='estado_create'),
    path('estado/editar/<int:id_estado>/', editarEstado, name='estado_edit'),
    path('municipio/nuevo/', crearMunicipio, name='municipio_create'),
    path('municipio/editar/<int:id_municipio>/', editarMunicipio, name='municipio_edit'),
    
]