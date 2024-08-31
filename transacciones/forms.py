from django import forms
from .models import MedioPago, FormaPago, Cotizacion, Proforma, Inventario, DetallesCotizacion, DetallesProforma

class MedioPagoForm(forms.ModelForm):
    class Meta:
        model = MedioPago
        fields = ['nombre', 'descripcion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class FormaPagoForm(forms.ModelForm):
    class Meta:
        model = FormaPago
        fields = ['id_fpago', 'nombre', 'descripcion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class CotizacionForm(forms.ModelForm):
    class Meta:
        model = Cotizacion
        fields = ['id_cotizacion', 'id_cliente', 'id_trabajador', 'fecha_emision', 'fecha_vencimiento', 'iva', 'estado']
        widgets = {
            'id_cliente': forms.Select(attrs={'class': 'form-control'}),
            'id_trabajador': forms.Select(attrs={'class': 'form-control'}),
            'fecha_emision': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'fecha_vencimiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'iva': forms.NumberInput(attrs={'class': 'form-control'}),
            'estado': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ProformaForm(forms.ModelForm):
    class Meta:
        model = Proforma
        fields = ['id_proforma', 'id_cliente', 'id_trabajador', 'id_mpago', 'id_fpago', 'fecha_emision', 'fecha_vencimiento', 'descuento', 'iva', 'estado']
        widgets = {
            'id_cliente': forms.Select(attrs={'class': 'form-control'}),
            'id_trabajador': forms.Select(attrs={'class': 'form-control'}),
            'id_mpago': forms.Select(attrs={'class': 'form-control'}),
            'id_fpago': forms.Select(attrs={'class': 'form-control'}),
            'fecha_emision': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'fecha_vencimiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'descuento': forms.NumberInput(attrs={'class': 'form-control'}),
            'iva': forms.NumberInput(attrs={'class': 'form-control'}),
            'estado': forms.TextInput(attrs={'class': 'form-control'}),
        }

class InventarioForm(forms.ModelForm):
    class Meta:
        model = Inventario
        fields = ['id_inventario', 'id_producto', 'fecha', 'id_proveedor', 'cantidad', 'n_lote', 'precio_cost']
        widgets = {
            'id_producto': forms.Select(attrs={'class': 'form-control'}),
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'id_proveedor': forms.Select(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'n_lote': forms.TextInput(attrs={'class': 'form-control'}),
            'precio_cost': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class DetallesCotizacionForm(forms.ModelForm):
    class Meta:
        model = DetallesCotizacion
        fields = ['id_dcotizacion', 'id_cotizacion', 'id_producto', 'cantidad', 'subtotal_prodc']
        widgets = {
            'id_cotizacion': forms.Select(attrs={'class': 'form-control'}),
            'id_producto': forms.Select(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'subtotal_prodc': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class DetallesProformaForm(forms.ModelForm):
    class Meta:
        model = DetallesProforma
        fields = ['id_dproforma', 'id_proforma', 'id_producto', 'cantidad', 'subtotal_prodprof']
        widgets = {
            'id_proforma': forms.Select(attrs={'class': 'form-control'}),
            'id_producto': forms.Select(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'subtotal_prodprof': forms.NumberInput(attrs={'class': 'form-control'}),
        }
