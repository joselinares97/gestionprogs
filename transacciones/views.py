from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.views import View
from django.urls import reverse
from .models import MedioPago, FormaPago, Inventario, Cotizacion, Proforma, DetallesCotizacion, DetallesProforma
from .forms import MedioPagoForm, FormaPagoForm, InventarioForm, CotizacionForm, ProformaForm, DetallesCotizacionForm, DetallesProformaForm
from django.db.models import ProtectedError

#Tabla de Medio de Pago

def crearMedioPago(request):
    if request.method == 'POST':
        MedioPago_Form = MedioPagoForm(request.POST)
        if MedioPago_Form.is_valid():
            MedioPago_Form.save()
            return redirect('mediopago_create')
    else:
        MedioPago_Form = MedioPagoForm()
        
    estadoFuncion = 'crear'
    MedioPago_Form = MedioPagoForm()
    mediospagos = MedioPago.objects.all()
    context = {
        'MedioPago_Form': MedioPago_Form,
        'estadoFuncion': estadoFuncion,
        'mediospagos': mediospagos,
    }
    
    return render(request, 'transacciones/mediopago_form.html', context)

def editarMedioPago(request, id_mpago):
    error = None
    try:
        mediopago_instance = MedioPago.objects.get(id_mpago=id_mpago)
        if request.method == 'GET':
            MedioPago_Form = MedioPagoForm(instance=mediopago_instance)
            estadoFuncion ='editar'
        else:
            MedioPago_Form = MedioPagoForm(request.POST, instance=mediopago_instance)
            estadoFuncion = 'editar'
            if MedioPago_Form.is_valid():
                MedioPago_Form.save()
                return redirect('mediopago_create')
    except ObjectDoesNotExist as e:
        error = 'El Medio de pago con el ID especificado no existe.'
        MedioPago_Form = MedioPagoForm()
        estadoFuncion = 'crear'
    
    mediospagos = MedioPago.objects.all()
    context = {
        'error': error,
        'MedioPago_Form': MedioPago_Form,
        'estadoFuncion': estadoFuncion,
        'mediospagos': mediospagos,
        'estadoFuncion': estadoFuncion,
    }
    
    return render(request, 'transacciones/mediopago_form.html', context)

def eliminarMedioPago(request, id_mpago):
    error = None
    if request.method == 'POST':
        try:
            mediopago_instance = MedioPago.objects.get(id_mpago=id_mpago)
            mediopago_instance.delete()
            return redirect('mediopago_create')
        except ObjectDoesNotExist:
            error = 'El medio de pago con el ID especificado no existe.'
        except ProtectedError:
            error = 'No se puede eliminar el medio de pago porque está en uso.'
            MedioPago_Form = MedioPagoForm()
    
    estadoFuncion = 'crear'
    mediospagos = MedioPago.objects.all()
    context = {
        'error': error,
        'MedioPago_Form': MedioPago_Form,
        'estadoFuncion': estadoFuncion,
        'mediospagos': mediospagos,
        'estadoFuncion': estadoFuncion,
    }
    
    return render(request, 'transacciones/mediopago_form.html', context)
