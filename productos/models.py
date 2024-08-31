from django.db import models

class Categoria(models.Model):
    id_cat = models.AutoField(db_column='Id_Cat', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=100, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'categoria'


class Productos(models.Model):
    id_producto = models.AutoField(db_column='Id_Producto', primary_key=True)  # Field name made lowercase.
    cod_producto = models.CharField(db_column='Cod_Producto', unique=True, max_length=50)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=100, blank=True, null=True)  # Field name made lowercase.
    marca = models.CharField(db_column='Marca', max_length=100, blank=True, null=True)  # Field name made lowercase.
    id_cat = models.ForeignKey(Categoria, models.DO_NOTHING, db_column='Id_Cat', blank=True, null=True)  # Field name made lowercase.
    stock = models.IntegerField(db_column='Stock', blank=True, null=True)  # Field name made lowercase.
    stock_min = models.IntegerField(db_column='Stock_min', blank=True, null=True)  # Field name made lowercase.
    stock_max = models.IntegerField(db_column='Stock_max', blank=True, null=True)  # Field name made lowercase.
    precio_venta = models.DecimalField(db_column='precio_Venta', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'productos'