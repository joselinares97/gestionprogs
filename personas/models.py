from django.db import models
from configuracion.models import TDocumento, TContribuyente, Municipio

class Cliente(models.Model):
    id_cliente = models.AutoField(db_column='Id_Cliente', primary_key=True)
    id_tdoc = models.ForeignKey(TDocumento, models.DO_NOTHING, db_column='Id_TDoc', blank=True, null=True)
    n_doccl = models.CharField(db_column='N_DocCl', unique=True, max_length=20)
    nombre = models.CharField(db_column='Nombre', max_length=100, blank=True, null=True)
    apellido = models.CharField(db_column='Apellido', max_length=100)
    id_tcont = models.ForeignKey(TContribuyente, models.DO_NOTHING, db_column='Id_TCont', blank=True, null=True)
    email = models.CharField(db_column='Email', max_length=100, blank=True, null=True)
    telefono = models.CharField(db_column='Telefono', max_length=20, blank=True, null=True)
    id_municipio = models.ForeignKey(Municipio, models.DO_NOTHING, db_column='Id_Municipio', blank=True, null=True)
    detalles_direccion = models.CharField(db_column='Detalles_direccion', max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cliente'

class Proveedor(models.Model):
    id_proveedor = models.AutoField(db_column='Id_Proveedor', primary_key=True)
    num_docpro = models.CharField(db_column='Num_DocPro', unique=True, max_length=20)
    id_tdoc = models.ForeignKey(TDocumento, models.DO_NOTHING, db_column='Id_TDoc', blank=True, null=True)
    nombre = models.CharField(db_column='Nombre', max_length=100, blank=True, null=True)
    id_tcont = models.ForeignKey(TContribuyente, models.DO_NOTHING, db_column='Id_TCont', blank=True, null=True)
    email = models.CharField(db_column='Email', max_length=100)
    telefono = models.CharField(db_column='Telefono', max_length=20, blank=True, null=True)
    id_municipio = models.ForeignKey(Municipio, models.DO_NOTHING, db_column='Id_Municipio', blank=True, null=True)
    detalles_direccion = models.CharField(db_column='Detalles_direccion', max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proveedor'
