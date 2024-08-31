from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.views import View
from django.urls import reverse
from .models import Categoria, Productos
from .forms import CategoriaForm, ProductosForm
from django.db.models import ProtectedError

#Create de la Tabla de Categoria
def crearCategoria(request):
    if request.method == 'POST':
        Categoria_Form = CategoriaForm(request.POST)
        if Categoria_Form.is_valid():
            Categoria_Form.save()
            return redirect('categoria_create')
    else:
        Categoria_Form = CategoriaForm()
    
    estadoFuncion = 'crear'
    categorias = Categoria.objects.all()
    
    context = {
        'Categoria_Form': Categoria_Form,
        'categorias': categorias,
        'estadoFuncion': estadoFuncion,
    }
    return render(request, 'productos/categoria_form.html', context)
    
def editarCategoria(request, id_cat):
    error = None
    try:
        categoria_instance = Categoria.objects.get(id_cat=id_cat)
        if request.method == 'GET':
            Categoria_Form = CategoriaForm(instance=categoria_instance)
            estadoFuncion = 'editar'
        else:
            Categoria_Form = CategoriaForm(request.POST, instance=categoria_instance)
            estadoFuncion = 'editar'
            if Categoria_Form.is_valid():
                Categoria_Form.save()
                return redirect('categoria_create')
    except ObjectDoesNotExist as e:
        error = 'La categoria con el ID especificado no existe.'
        Categoria_Form = CategoriaForm()
        estadoFuncion = 'crear'
    
    categorias = Categoria.objects.all()
    
    context = {
        'Categoria_Form': Categoria_Form,
        'categorias': categorias,
        'estadoFuncion': estadoFuncion,
        'error': error,
    }
    return render(request, 'productos/categoria_form.html', context)

def eliminarCategoria(request, id_cat):
    error = None
    if request.method == 'POST':
        try:
            categoria_instance = Categoria.objects.get(id_cat=id_cat)
            categoria_instance.delete()
            return redirect('categoria_create')
        except ObjectDoesNotExist:
            error = 'La categoría con el ID especificado no existe.'
        except ProtectedError:
            error = 'No se puede eliminar la categoría porque está en uso.'

    Categoria_Form = CategoriaForm()
    categorias = Categoria.objects.all()
    
    context = {
        'Categoria_Form': Categoria_Form,
        'categorias': categorias,
        'estadoFuncion': 'crear',
        'error': error,
    }
    return render(request, 'productos/categoria_form.html', context)


#Create de la Tabla Productos
def crearProducto(request):
    if request.method == 'POST':
        Productos_Form = ProductosForm(request.POST)
        if Productos_Form.is_valid():
            Productos_Form.save()
            return redirect('producto_create')
    else:
        Productos_Form = ProductosForm()
    
    productos = Productos.objects.all()
    categorias = Categoria.objects.all()
    estadoFuncion = 'crear'
    
    context = {
        'Productos_Form': Productos_Form,
        'productos': productos,
        'categorias': categorias,
        'estadoFuncion': estadoFuncion,
    }
    
    return render(request, 'productos/productos_form.html', context)

def editarProducto(request, id_producto):
    error = None
    try:
        productos_instance = Productos.objects.get(id_producto=id_producto)
        if request.method == 'GET':
            Productos_Form = ProductosForm(instance= productos_instance)
            estadoFuncion = 'editar'
        else:
            Productos_Form = ProductosForm(request.POST, instance=productos_instance)
            estadoFuncion = 'editar'
            if Productos_Form.is_valid():
                Productos_Form.save()
                return redirect('producto_create')
    except ObjectDoesNotExist as e:
        error = 'El producto con el ID especificado no existe.'
        Productos_Form = ProductosForm()
        estadoFuncion = 'editar'
    
    productos = Productos.objects.all()
    categorias = Categoria.objects.all()
    context = {
        'Productos_Form': Productos_Form,
        'productos': productos,
        'estadoFuncion': estadoFuncion,
        'error': error,
        'categorias': categorias,
    }
    return render(request, 'productos/productos_form.html', context)

def eliminarProducto(request, id_producto):
    error = None
    if request.method == 'POST':
        try:
            producto_instance = Productos.objects.get(id_producto=id_producto)
            producto_instance.delete()
            return redirect('producto_create')
        except ObjectDoesNotExist:
            error = 'El producto con el ID especificado no existe.'
        except ProtectedError:
            'No se puede eliminar el producto porque está en uso.'
    productos = Productos.objects.all()
    Productos_Form = ProductosForm()
    estadoFuncion = 'crear'
    context = {
        'Productos_Form': Productos_Form,
        'productos': productos,
        'estadoFuncion': estadoFuncion,
        'error': error,
    }
    return render(request, 'productos/productos_form.html', context)
