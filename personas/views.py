from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.views import View
from django.urls import reverse
from .models import Cliente, Municipio, TDocumento, TContribuyente, Proveedor
from .forms import ClienteForm, ProveedorForm

# Create, Read, Update, Delete de Clientes
def crearCliente(request):
    if request.method == 'POST':
        Cliente_Form = ClienteForm(request.POST)
        if Cliente_Form.is_valid():
            Cliente_Form.save()
            return redirect('cliente_create')
    else:
        Cliente_Form = ClienteForm()

    clientes = Cliente.objects.all()
    municipios = Municipio.objects.all()
    tdocumentos = TDocumento.objects.all()
    tcontribuyentes = TContribuyente.objects.all()
    estadoFuncion = 'crear'

    context = {
        'Cliente_Form': Cliente_Form,
        'clientes': clientes,
        'municipios': municipios,
        'tdocumentos': tdocumentos,
        'tcontribuyentes': tcontribuyentes,
        'estadoFuncion': estadoFuncion,
    }
    return render(request, 'personas/cliente_form.html', context)

def editarCliente(request, id_cliente):
    Cliente_Form = None
    error = None
    try:
        cliente_instance = Cliente.objects.get(id_cliente=id_cliente)
        if request.method == 'GET':
            Cliente_Form = ClienteForm(instance=cliente_instance)
        else:
            Cliente_Form = ClienteForm(request.POST, instance=cliente_instance)
            if Cliente_Form.is_valid():
                Cliente_Form.save()
                return redirect('cliente_create')
    except ObjectDoesNotExist as e:
        error = 'El cliente con el ID especificado no existe.'
    
    clientes = Cliente.objects.all()
    municipios = Municipio.objects.all()
    tdocumentos = TDocumento.objects.all()
    tcontribuyentes = TContribuyente.objects.all()
    estadoFuncion = 'crear'

    context = {
        'Cliente_Form': Cliente_Form,
        'clientes': clientes,
        'municipios': municipios,
        'tdocumentos': tdocumentos,
        'tcontribuyentes': tcontribuyentes,
        'estadoFuncion': estadoFuncion,
    }
    return render(request, 'personas/cliente_form.html', context)

def eliminarCliente(request):
    error = None
    if request.method == 'POST':
        id_cliente = request.POST.get('id_cliente')
        try:
            cliente_instance = Cliente.objects.get(id_cliente=id_cliente)
            cliente_instance.delete()
            return redirect('cliente_create')
        except ObjectDoesNotExist:
            error = "El Cliente con el ID especificado no existe."
   
    clientes = Cliente.objects.all()
    municipios = Municipio.objects.all()
    tdocumentos = TDocumento.objects.all()
    tcontribuyentes = TContribuyente.objects.all()
    estadoFuncion = 'crear'

    context = {
        'Cliente_Form': cliente_instance,
        'clientes': clientes,
        'municipios': municipios,
        'tdocumentos': tdocumentos,
        'tcontribuyentes': tcontribuyentes,
        'estadoFuncion': estadoFuncion,
    }
    return render(request, 'personas/cliente_form.html', context)

# Create, Read, Update, Delete de Proveedores

def crearProveedor(request):
    if request.method == 'POST':
        Proveedor_Form = ProveedorForm(request.POST)
        if Proveedor_Form.is_valid():
            Proveedor_Form.save()
            return redirect('proveedor_create')
    else:
        Proveedor_Form = ClienteForm()
    
    proveedores = Proveedor.objects.all()
    municipios = Municipio.objects.all()
    tdocumentos = TDocumento.objects.all()
    tcontribuyentes = TContribuyente.objects.all()
    estadoFuncion = 'crear'

    context = {
        'Proveedor_Form': Proveedor_Form,
        'proveedores': proveedores,
        'municipios': municipios,
        'tdocumentos': tdocumentos,
        'tcontribuyentes': tcontribuyentes,
        'estadoFuncion': estadoFuncion,
    }
    
    return render(request, 'personas/proveedor_form.html', context)

def editarProveedor(request, id_proveedor):
    Proveedor_Form = None
    error = None
    try:
        proveedor_instance = Proveedor.objects.get(id_proveedor=id_proveedor)
        if request.method == 'GET':
            Proveedor_Form = ProveedorForm(instance=proveedor_instance)
        else:
            Proveedor_Form = ProveedorForm(request.POST, instance=proveedor_instance)
            if Proveedor_Form.is_valid():
                Proveedor_Form.save()
                return redirect('proveedor_create')
    except ObjectDoesNotExist as e:
        error = 'El proveedor con el ID especificado no existe.'
        
    proveedores = Proveedor.objects.all()
    municipios = Municipio.objects.all()
    tdocumentos = TDocumento.objects.all()
    tcontribuyentes = TContribuyente.objects.all()
    estadoFuncion = 'crear'

    context = {
        'Proveedor_Form': Proveedor_Form,
        'proveedores': proveedores,
        'municipios': municipios,
        'tdocumentos': tdocumentos,
        'tcontribuyentes': tcontribuyentes,
        'estadoFuncion': estadoFuncion,
    }
    
    return render(request, 'personas/proveedor_form.html', context)

def eliminarProveedor(request):
    error = None
    if request.method == 'POST':
        id_proveedor = request.POST.get('id_proveedor')
        try:
            proveedor_instance = Proveedor.objects.get(id_proveedor=id_proveedor)
            proveedor_instance.delete()
            return redirect('proveedor_create')
        except ObjectDoesNotExist:
            error = 'El proveedor con el ID especificado no existe.'
    
    proveedores = Proveedor.objects.all()
    municipios = Municipio.objects.all()
    tdocumentos = TDocumento.objects.all()
    tcontribuyentes = TContribuyente.objects.all()
    estadoFuncion = 'crear'

    context = {
        'Proveedor_Form': proveedor_instance,
        'proveedores': proveedores,
        'municipios': municipios,
        'tdocumentos': tdocumentos,
        'tcontribuyentes': tcontribuyentes,
        'estadoFuncion': estadoFuncion,
    }
    
    return render(request, 'personas/proveedor_form.html', context)
