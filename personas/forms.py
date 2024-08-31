from django import forms
from .models import Cliente, Proveedor

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['id_tdoc', 'n_doccl', 'nombre', 'apellido', 'id_tcont', 'email', 'telefono', 'id_municipio', 'detalles_direccion']
        widgets = {
            'id_tdoc': forms.Select(attrs={'class': 'form-control'}),
            'id_tcont': forms.Select(attrs={'class': 'form-control'}),
            'id_municipio': forms.Select(attrs={'class': 'form-control'}),
        }
        
class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['id_proveedor', 'num_docpro', 'id_tdoc', 'nombre', 'id_tcont', 'email', 'telefono', 'id_municipio', 'detalles_direccion']
        widgets = {
            'id_tdoc': forms.Select(attrs={'class': 'form-control'}),
            'id_tcont': forms.Select(attrs={'class': 'form-control'}),
            'id_municipio': forms.Select(attrs={'class': 'form-control'}),
            'num_docpro': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'detalles_direccion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }