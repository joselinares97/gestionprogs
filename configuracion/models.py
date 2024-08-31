from django.db import models

class TContribuyente(models.Model):
    id_tcont = models.AutoField(db_column='Id_TCont', primary_key=True)
    nombre = models.CharField(db_column='Nombre', max_length=100, blank=True, null=True)
    descripcion = models.CharField(db_column='Descripcion', max_length=255, blank=True, null=True)

    def __str__(self):
        return self.nombre if self.nombre else str(self.id_tcont)

    class Meta:
        managed = False
        db_table = 't_contribuyente'

class TDocumento(models.Model):
    id_tdoc = models.AutoField(db_column='Id_TDoc', primary_key=True)
    nombre = models.CharField(db_column='Nombre', max_length=100, blank=True, null=True)
    descripcion = models.CharField(db_column='Descripcion', max_length=255, blank=True, null=True)

    def __str__(self):
        return self.nombre if self.nombre else str(self.id_tdoc)

    class Meta:
        managed = False
        db_table = 't_documento'

class Pais(models.Model):
    id_pais = models.AutoField(db_column='Id_Pais', primary_key=True)
    nombre = models.CharField(db_column='Nombre', max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nombre if self.nombre else str(self.id_pais)

    class Meta:
        managed = False
        db_table = 'pais'

class Estado(models.Model):
    id_estado = models.AutoField(db_column='Id_Estado', primary_key=True)
    nombre = models.CharField(db_column='Nombre', max_length=100, blank=True, null=True)
    id_pais = models.ForeignKey(Pais, models.DO_NOTHING, db_column='Id_Pais', blank=True, null=True)

    def __str__(self):
        return self.nombre if self.nombre else str(self.id_estado)

    class Meta:
        managed = False
        db_table = 'estado'

class Municipio(models.Model):
    id_municipio = models.AutoField(db_column='Id_Municipio', primary_key=True)
    nombre = models.CharField(db_column='Nombre', max_length=100, blank=True, null=True)
    id_estado = models.ForeignKey(Estado, models.DO_NOTHING, db_column='Id_Estado', blank=True, null=True)

    def __str__(self):
        return self.nombre if self.nombre else str(self.id_municipio)

    class Meta:
        managed = False
        db_table = 'municipio'
