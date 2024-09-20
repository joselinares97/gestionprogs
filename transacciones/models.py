from django.db import models
from personas.models import Cliente, Proveedor
from usuarios.models import Trabajador
from productos.models import Productos


class MedioPago(models.Model):
    id_mpago = models.AutoField(db_column='Id_MPago', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=100, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'medio_pago'


class FormaPago(models.Model):
    id_fpago = models.AutoField(db_column='Id_FPago', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=100, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'forma_pago'


class Cotizacion(models.Model):
    id_cotizacion = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING, db_column='Id_Cliente', blank=True, null=True)
    id_trabajador = models.ForeignKey(Trabajador, on_delete=models.DO_NOTHING, db_column='Id_trabajador', blank=True, null=True)
    fecha_emision = models.DateField(db_column='Fecha_emision', blank=True, null=True)
    fecha_vencimiento = models.DateField(db_column='Fecha_vencimiento', blank=True, null=True)
    iva = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    estado = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'cotizacion'

        

class Proforma(models.Model):
    id_proforma = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING, db_column='Id_Cliente', blank=True, null=True)
    id_trabajador = models.ForeignKey(Trabajador, on_delete=models.DO_NOTHING, db_column='Id_trabajador', blank=True, null=True)
    id_mpago = models.ForeignKey(MedioPago, on_delete=models.DO_NOTHING, db_column='Id_MPago', blank=True, null=True)
    id_fpago = models.ForeignKey(FormaPago, on_delete=models.DO_NOTHING, db_column='Id_FPago', blank=True, null=True)
    fecha_emision = models.DateField(db_column='Fecha_emision', blank=True, null=True)
    fecha_vencimiento = models.DateField(db_column='Fecha_vencimiento', blank=True, null=True)
    descuento = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    iva = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    estado = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proforma'

        
class Inventario(models.Model):
    id_inventario = models.AutoField(primary_key=True)
    id_producto = models.ForeignKey(Productos, on_delete=models.DO_NOTHING, db_column='id_Producto', blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    id_proveedor = models.ForeignKey(Proveedor, on_delete=models.DO_NOTHING, db_column='id_Proveedor', blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)
    n_lote = models.CharField(max_length=50, blank=True, null=True)
    precio_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inventario'


class DetallesCotizacion(models.Model):
    id_dcotizacion = models.AutoField(primary_key=True)
    id_cotizacion = models.ForeignKey(Cotizacion, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Productos, on_delete=models.CASCADE)  # Relación con Productos
    cantidad = models.IntegerField()
    subtotal_prodc = models.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        managed = False
        db_table = 'detalles_cotizacion'



class DetallesProforma(models.Model):
    id_dproforma = models.AutoField(primary_key=True)
    id_proforma = models.ForeignKey(Proforma, on_delete=models.DO_NOTHING, db_column='Id_Proforma', blank=True, null=True)
    id_producto = models.ForeignKey(Productos, on_delete=models.DO_NOTHING, db_column='Id_Producto', blank=True, null=True)
    cantidad = models.IntegerField(db_column='Cantidad', blank=True, null=True)
    subtotal_prodprof = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detalles_proforma'

