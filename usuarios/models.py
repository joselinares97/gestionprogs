from django.db import models

class TipoUsuario(models.Model):
    id_tuser = models.AutoField(db_column='Id_TUser', primary_key=True)
    nombre = models.CharField(db_column='Nombre', max_length=100, blank=True, null=True)
    descripcion = models.CharField(db_column='Descripcion', max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_usuario'


class Trabajador(models.Model):
    id_trabajador = models.AutoField(db_column='Id_Trabajador', primary_key=True)
    num_doctrab = models.CharField(db_column='Num_DocTrab', unique=True, max_length=20)
    id_tdoc = models.ForeignKey('configuracion.TDocumento', models.DO_NOTHING, db_column='Id_TDoc', blank=True, null=True)
    nombre = models.CharField(db_column='Nombre', max_length=100, blank=True, null=True)
    apellido = models.CharField(db_column='Apellido', max_length=100)
    email = models.CharField(db_column='Email', max_length=100, blank=True, null=True)
    telefono = models.CharField(db_column='Telefono', max_length=20, blank=True, null=True)
    id_municipio = models.ForeignKey('configuracion.Municipio', models.DO_NOTHING, db_column='Id_Municipio', blank=True, null=True)
    detalles_direccion = models.CharField(db_column='Detalles_direccion', max_length=255, blank=True, null=True)
    id_tuser = models.ForeignKey(TipoUsuario, models.DO_NOTHING, db_column='Id_TUser', blank=True, null=True)
    id_usuario = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='Id_Usuario', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trabajador'


class Usuarios(models.Model):
    id_usuario = models.AutoField(db_column='Id_Usuario', primary_key=True)
    usuario = models.CharField(db_column='Usuario', unique=True, max_length=50)
    contrasena = models.CharField(db_column='Contrasena', max_length=255)
    id_trabajador = models.ForeignKey(Trabajador, models.DO_NOTHING, db_column='Id_Trabajador', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuarios'
