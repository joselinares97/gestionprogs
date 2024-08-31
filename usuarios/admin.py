from django.contrib import admin
from .models import TipoUsuario, Trabajador, Usuarios

admin.site.register(Usuarios)
admin.site.register(TipoUsuario)
admin.site.register(Trabajador)