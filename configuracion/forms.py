from django import forms
from .models import TContribuyente, TDocumento, Pais, Estado, Municipio

class TContribuyenteForm(forms.ModelForm):
    class Meta:
        model = TContribuyente
        fields = ['id_tcont','nombre', 'descripcion']
        
class TDocumentoForm(forms.ModelForm):
    class Meta:
        model = TDocumento
        fields =['id_tdoc', 'nombre', 'descripcion']
        
class PaisForm(forms.ModelForm):
    class Meta:
        model = Pais
        fields = ['id_pais', 'nombre',]
        
class EstadoForm(forms.ModelForm):
    class Meta:
        model = Estado
        fields = ['id_estado', 'nombre', 'id_pais']
        widgets = {
            'id_pais': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(EstadoForm, self).__init__(*args, **kwargs)
        self.fields['id_pais'].queryset = Pais.objects.all()
        self.fields['id_pais'].label_from_instance = lambda obj: "%s" % obj.nombre

        default_pais = Pais.objects.filter(nombre="Colombia").first()
        if default_pais:
            self.fields['id_pais'].initial = default_pais.id_pais
            
class MunicipioForm(forms.ModelForm):
    class Meta:
        model = Municipio
        fields = ['id_municipio', 'nombre', 'id_estado']
        widgets = {
            'id_estado': forms.Select(attrs={'class': 'forms-control'}),
        }
        
    def __init__(self, *args, **kwargs):
        super(MunicipioForm, self).__init__(*args, **kwargs)
        self.fields['id_estado'].queryset = Estado.objects.all()
        self.fields['id_estado'].label_from_instance = lambda obj: "%s" % obj.nombre

        default_estado = Estado.objects.filter(nombre="Bogota").first()
        if default_estado:
            self.fields['id_estado'].initial = default_estado.id_estado