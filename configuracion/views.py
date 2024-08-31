from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.views import View
from django.urls import reverse
from .models import TContribuyente, TDocumento, Pais, Estado, Municipio
from .forms import TContribuyenteForm, TDocumentoForm, PaisForm, EstadoForm, MunicipioForm

#Create de la tabla Tipo de Contribuyente 'TContribuyente'
def crearTContribuyente(request):
        if request.method == 'POST':
            TContribuyente_Form = TContribuyenteForm(request.POST)
            if TContribuyente_Form.is_valid():
                TContribuyente_Form.save()
                return redirect('tcontribuyente_create')
        else:
            TContribuyente_Form = TContribuyenteForm()
            
        tcontribuyentes = TContribuyente.objects.all()
        estadoFuncion = 'crear'
        
        context = {
            'TContribuyente_Form': TContribuyente_Form,
            'tcontribuyentes': tcontribuyentes,
            'estadoFuncion': estadoFuncion,
        }
        return render(request,'configuracion/tcontribuyente_form.html', context)

def editarTContribuyente(request, id_tcont):
        TContribuyente_Form = None
        error = None
        try:
            tcontribuyente_instance = TContribuyente.objects.get(id_tcont=id_tcont)
            if request.method == 'GET':
                TContribuyente_Form = TContribuyenteForm(instance=tcontribuyente_instance)
            else:
                TContribuyente_Form = TContribuyenteForm(request.POST, instance=tcontribuyente_instance)
                if TContribuyente_Form.is_valid():
                    TContribuyente_Form.save()
                    return redirect('tcontribuyente_create')
        except ObjectDoesNotExist as e:
            error = "El contribuyente con el ID especificado no existe."
        tcontribuyentes = TContribuyente.objects.all()
        estadoFuncion = 'crear'

        context = {
            'TContribuyente_Form': TContribuyente_Form,
            'tcontribuyentes': tcontribuyentes,
            'estadoFuncion': estadoFuncion,
        }
        return render(request, 'configuracion/tcontribuyente_form.html', context)

def eliminarTContribuyente(request):
        error = None
        if request.method == 'POST':
            id_tcont = request.POST.get('id_tcont')
            try:
                tcontribuyente_instance = TContribuyente.objects.get(id_tcont=id_tcont)
                tcontribuyente_instance.delete()
                return redirect('tcontribuyente_create')
            except ObjectDoesNotExist:
                error = "El contribuyente con el ID especificado no existe."

        tcontribuyentes = TContribuyente.objects.all()
        estadoFuncion = 'crear'

        context = {
            'tcontribuyentes': tcontribuyentes,
            'estadoFuncion': estadoFuncion,
            'error': error,
        }
        return render(request, 'configuracion/tcontribuyente_form.html', context)

#Create, Read, Update de la tabla de Tipo de Documento 'TDocumento'


def crearTDocumento(request):
    if request.method == 'POST':
        TDocumento_Form = TDocumentoForm(request.POST)
        if TDocumento_Form.is_valid():
            TDocumento_Form.save()
            return redirect('tdocumento_create')
    else:
        TDocumento_Form = TDocumentoForm()
    
    tdocumentos = TDocumento.objects.all()
    estadoFuncion = 'crear'
    
    context = {
        'TDocumento_Form': TDocumento_Form,
        'tdocumentos': tdocumentos,
        'estadoFuncion': estadoFuncion,
    }
    return render(request, 'configuracion/tdocumento_form.html', context)

def editarTDocumento(request, id_tdoc):
    TDocumento_Form = None
    error = None
    try:
        tdocumento_instance = TDocumento.objects.get(id_tdoc=id_tdoc)
        if request.method == 'GET':
            TDocumento_Form = TDocumentoForm(instance=tdocumento_instance)
        else:
            TDocumento_Form = TDocumentoForm(request.POST, instance=tdocumento_instance)
            if TDocumento_Form.is_valid():
                TDocumento_Form.save()
                return redirect('tdocumento_create')
    except ObjectDoesNotExist as e:
        error = 'El tipo de documento con el ID especificado no existe.'
    tdocumentos = TDocumento.objects.all()
    estadoFuncion = 'crear'
    
    context = {
        'TDocumento_Form' : TDocumento_Form ,
        'tdocumentos' : tdocumentos,
        'estadoFuncion': estadoFuncion,
    }
    return render(request, 'configuracion/tdocumento_form.html', context)

def eliminarTDocumento(request):
    error = None
    if request.method == 'POST':
        id_tdoc = request.POST.get('id_tdoc')
        try:
            tdocumento_instance = TDocumento.objects.get(id_tdoc=id_tdoc)
            tdocumento_instance.delete()
            return redirect('tdocumento_create')
        except ObjectDoesNotExist:
            error = "El tipo de documento con el ID especificado no existe."

    tdocumentos = TDocumento.objects.all()
    estadoFuncion = 'crear'

    context = {
        'tdocumentos': tdocumentos,
        'estadoFuncion': estadoFuncion,
        'error': error,
    }
    return render(request, 'configuracion/tdocumento_form.html', context)



#Create, Read, Update de la tabla Pais 'Pais'

def crearPais(request):
    if request.method == 'POST':
        Pais_Form = PaisForm(request.POST)
        if Pais_Form.is_valid():
            Pais_Form.save()
            return redirect('pais_create')
    else:
        Pais_Form = PaisForm()

    paises = Pais.objects.all()
    estadoFuncion = 'crear'
    context = {
        'Pais_Form': Pais_Form,
        'paises': paises,
        'estadoFuncion': estadoFuncion,
    }
    return render(request, 'configuracion/pais_form.html', context)

def editarPais(request, id_pais):
    Pais_Form = None
    error = None
    try:
        pais_instance= Pais.objects.get(id_pais=id_pais)
        if request.method == 'GET':
            Pais_Form = PaisForm(instance=pais_instance)
        else:
            Pais_Form = PaisForm(request.POST, instance=pais_instance)
            if Pais_Form.is_valid():
                Pais_Form.save()
                return redirect('pais_create')
    except ObjectDoesNotExist as e:
        error = 'El pais con el ID espacificado no existe.'
    paises = Pais.objects.all()
    estadoFuncion = 'crear'
    context = {
        'Pais_Form': Pais_Form,
        'paises': paises,
        'estadoFuncion': estadoFuncion,
    }
    return render(request, 'configuracion/pais_form.html', context)

#Create, Read, Update de la tabla Estado 'Estado'

def crearEstado(request):
    error = None
    if request.method == 'POST':
        Estado_Form = EstadoForm(request.POST)
        if Estado_Form.is_valid():
            Estado_Form.save()
            return redirect('estado_create')  # Asegúrate de que esta URL existe
        else:
            error = "Hay un error en el formulario. Por favor, corríjalo."
    else:
        Estado_Form = EstadoForm()
        
    estados = Estado.objects.all()
    estadoFuncion = 'crear'
    
    context = {
        'Estado_Form': Estado_Form,
        'estados': estados,
        'error': error,
        'estadoFuncion': estadoFuncion,
    }
    return render(request, 'configuracion/estado_form.html', context)

def editarEstado(request, id_estado):
    error = None
    try:
        estado_instance = Estado.objects.get(id_estado=id_estado)
        if request.method == 'GET':
            Estado_Form = EstadoForm(instance=estado_instance)
        else:
            Estado_Form = EstadoForm(request.POST, instance=estado_instance)
            if Estado_Form.is_valid():
                Estado_Form.save()
                return redirect('estado_create')  # Asegúrate de que esta URL existe
            else:
                error = "Hay un error en el formulario. Por favor, corríjalo."
    except ObjectDoesNotExist:
        error = 'El Estado con el ID especificado no existe.'
    
    estados = Estado.objects.all()
    estadoFuncion = 'editar'
    context = {
        'Estado_Form': Estado_Form,
        'estados': estados,
        'error': error,
        'estadoFuncion': estadoFuncion,
    }
    return render(request, 'configuracion/estado_form.html', context)

#Create, Read, Update de la tabla Estado 'Municipio'
def crearMunicipio(request):
    error = None
    if request.method == 'POST':
        Municipio_Form = MunicipioForm(request.POST)
        if Municipio_Form.is_valid():
            Municipio_Form.save()
            return redirect('municipio_create')  # Asegúrate de que esta URL exista y sea correcta
        else:
            error = "Hay un error en el formulario. Por favor, corríjalo."
    else:
        Municipio_Form = MunicipioForm()

    municipios = Municipio.objects.all()
    estadoFuncion = 'crear'
    
    context = {
        'Municipio_Form': Municipio_Form,
        'municipios': municipios,
        'error': error,
        'estadoFuncion': estadoFuncion,
    }
    return render(request, 'configuracion/municipio_form.html', context)


def editarMunicipio(request, id_municipio):
    error = None
    try:
        municipio_instance = Municipio.objects.get(id_municipio=id_municipio)
        if request.method == 'GET':
            Municipio_Form = MunicipioForm(instance=municipio_instance)
        else:
            Municipio_Form = MunicipioForm(request.POST, instance=municipio_instance)
            if Municipio_Form.is_valid():
                Municipio_Form.save()
                return redirect('municipio_create')  # Asegúrate de que esta URL existe
            else:
                error = "Hay un error en el formulario. Por favor, corríjalo."
    except ObjectDoesNotExist:
        error = 'El Estado con el ID especificado no existe.'
    
    municipios = Municipio.objects.all()
    estadoFuncion = 'editar'
    context = {
        'Municipio_Form': Municipio_Form,
        'municipios': municipios,
        'error': error,
        'estadoFuncion': estadoFuncion,
    }
    return render(request, 'configuracion/municipio_form.html', context)