from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import index, dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),  # Ruta para la página de inicio
    path('dashboard/', dashboard, name='dashboard'),
    path('configuracion/', include('configuracion.urls')),
    path('personas/', include('personas.urls')),
    path('productos/', include('productos.urls')),
    path('transacciones/', include('transacciones.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
