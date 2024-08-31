from django import forms
from .models import Categoria, Productos

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion']
        labels = {
            'nombre': 'Nombre de la Categoría',
            'descripcion': 'Descripción de la Categoría'
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
        
class ProductosForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = ['id_producto', 'cod_producto', 'nombre', 'marca', 'id_cat', 'stock', 'stock_min', 'stock_max', 'precio_venta']
        
    def __init__(self, *args, **kwargs):
        super(ProductosForm, self).__init__(*args, **kwargs)
        self.fields['id_cat'].queryset = Categoria.objects.all()
        self.fields['id_cat'].label_from_instance = lambda obj: "%s" % obj.nombre
