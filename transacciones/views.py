from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.urls import reverse
from django.forms import modelformset_factory
from .models import MedioPago, FormaPago, Inventario, Cotizacion, Proforma, DetallesCotizacion, DetallesProforma, Trabajador, Productos, Cliente
from .forms import MedioPagoForm, FormaPagoForm, InventarioForm, CotizacionForm, ProformaForm, DetallesCotizacionForm, DetallesProformaForm
from django.db.models import ProtectedError
from personas.models import Cliente

# Tabla de Medio de Pago

def crearMedioPago(request):
    if request.method == 'POST':
        MedioPago_Form = MedioPagoForm(request.POST)
        if MedioPago_Form.is_valid():
            MedioPago_Form.save()
            return redirect('mediopago_create')
    else:
        MedioPago_Form = MedioPagoForm()
        
    mediospagos = MedioPago.objects.all()
    context = {
        'MedioPago_Form': MedioPago_Form,
        'estadoFuncion': 'crear',
        'mediospagos': mediospagos,
    }
    
    return render(request, 'transacciones/mediopago_form.html', context)

def editarMedioPago(request, id_mpago):
    error = None
    try:
        mediopago_instance = MedioPago.objects.get(id_mpago=id_mpago)
        if request.method == 'POST':
            MedioPago_Form = MedioPagoForm(request.POST, instance=mediopago_instance)
            if MedioPago_Form.is_valid():
                MedioPago_Form.save()
                return redirect('mediopago_create')
        else:
            MedioPago_Form = MedioPagoForm(instance=mediopago_instance)
        estadoFuncion = 'editar'
    except ObjectDoesNotExist:
        error = 'El Medio de pago con el ID especificado no existe.'
        MedioPago_Form = MedioPagoForm()
        estadoFuncion = 'crear'
    
    mediospagos = MedioPago.objects.all()
    context = {
        'error': error,
        'MedioPago_Form': MedioPago_Form,
        'estadoFuncion': estadoFuncion,
        'mediospagos': mediospagos,
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
    mediospagos = MedioPago.objects.all()
    context = {
        'error': error,
        'MedioPago_Form': MedioPago_Form,
        'estadoFuncion': 'crear',
        'mediospagos': mediospagos,
    }
    
    return render(request, 'transacciones/mediopago_form.html', context)

# Tabla de Formas de Pago

def crearFormaPago(request):
    if request.method == 'POST':
        FormaPago_Form = FormaPagoForm(request.POST)
        if FormaPago_Form.is_valid():
            FormaPago_Form.save()
            return redirect('formapago_create')
    else:
        FormaPago_Form = FormaPagoForm()
    
    formaspagos = FormaPago.objects.all()
    context = {
        'estadoFuncion': 'crear',
        'FormaPago_Form': FormaPago_Form,
        'formaspagos': formaspagos,
    }
    return render(request, 'transacciones/formapago_form.html', context)

def editarFormaPago(request, id_fpago):
    error = None
    try:
        formapago_instance = FormaPago.objects.get(id_fpago=id_fpago)
        if request.method == 'POST':
            FormaPago_Form = FormaPagoForm(request.POST, instance=formapago_instance)
            if FormaPago_Form.is_valid():
                FormaPago_Form.save()
                return redirect('formapago_create')
        else:
            FormaPago_Form = FormaPagoForm(instance=formapago_instance)
        estadoFuncion = 'editar'
    except ObjectDoesNotExist:
        error = 'La forma de pago con el ID especificado no existe.'
        FormaPago_Form = FormaPagoForm()
        estadoFuncion = 'crear'
    
    formaspagos = FormaPago.objects.all()
    context = {
        'error': error,
        'FormaPago_Form': FormaPago_Form,
        'estadoFuncion': estadoFuncion,
        'formaspagos': formaspagos,
    }
    return render(request, 'transacciones/formapago_form.html', context)

def eliminarFormaPago(request, id_fpago):
    error = None
    if request.method == 'POST':
        try:
            formapago_instance = FormaPago.objects.get(id_fpago=id_fpago)
            formapago_instance.delete()
            return redirect('formapago_create')
        except ObjectDoesNotExist:
            error = 'La forma de pago con el ID especificado no existe.'
        except ProtectedError:
            error = 'No se puede eliminar la forma de pago porque está en uso.'
    
    FormaPago_Form = FormaPagoForm()
    formaspagos = FormaPago.objects.all()
    context = {
        'error': error,
        'FormaPago_Form': FormaPago_Form,
        'estadoFuncion': 'crear',
        'formaspagos': formaspagos,
    }
    return render(request, 'transacciones/formapago_form.html', context)

@csrf_exempt  # Desactiva CSRF para pruebas. Usa un token CSRF válido en producción.
def cotizacionDetalles(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            cotizacion_form = CotizacionForm(data)

            if cotizacion_form.is_valid():
                # Guardar la cotización
                cotizacion = cotizacion_form.save()

                # Procesar los detalles de los productos
                for detalle_data in data['detalles']:
                    try:
                        producto = Productos.objects.get(id_producto=detalle_data['id_producto'])
                        DetallesCotizacion.objects.create(
                            id_cotizacion=cotizacion,
                            id_producto=producto,
                            cantidad=detalle_data['cantidad'],
                            subtotal_prodc=detalle_data['subtotal_descuento']
                        )
                    except Productos.DoesNotExist:
                        return JsonResponse({'success': False, 'error': 'Producto no encontrado'}, status=400)

                return JsonResponse({'success': True})

            else:
                return JsonResponse({'success': False, 'errors': cotizacion_form.errors})

        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'error': 'Error al procesar JSON'}, status=400)

    else:
        cotizacion_form = CotizacionForm()
        return render(request, 'transacciones/cotizacion_form.html', {'cotizacion_form': cotizacion_form})

def cotizacion_list(request):
    cotizaciones = Cotizacion.objects.all()
    return render(request, 'transacciones/cotizacion_list.html', {'cotizaciones': cotizaciones})



#Filtro de Busqueda de Productos
def buscar_productos(request):
    query = request.GET.get('query', '')
    
    if query:
        productos = Productos.objects.filter(
            nombre__icontains=query
        ) | Productos.objects.filter(
            cod_producto__icontains=query
        )
    else:
        productos = Productos.objects.none()  # Si no hay query, no devolver ningún producto

    data = list(productos.values('id_producto', 'nombre', 'cod_producto', 'precio_venta'))
    return JsonResponse(data, safe=False)



#Filtro de Busqueda de Clientes
def buscar_cliente(request):
    query = request.GET.get('q', '')
    
    if query:
        clientes = Cliente.objects.filter(
            n_doccl__icontains=query
        ) | Cliente.objects.filter(
            nombre__icontains=query
        )
    else:
        clientes = Cliente.objects.none()  # Si no hay query, no devolver ningún cliente

    data = list(clientes.values('id_cliente', 'nombre', 'apellido', 'telefono', 'n_doccl'))
    return JsonResponse(data, safe=False)



def get_productos(request):
    ids = request.GET.get('ids', '')
    id_list = ids.split(',')
    productos = Productos.objects.filter(id__in=id_list).values('id', 'nombre', 'codigo')
    return JsonResponse({'productos': list(productos)})

def select_products(request):
    return render(request, 'transacciones/select_products.html')

def get_producto_info(request):
    producto_id = request.GET.get('id')
    try:
        producto = Productos.objects.get(id_producto=producto_id)
        data = {
            'nombre': producto.nombre,
            'cod_producto': producto.cod_producto,
            'precio_venta': producto.precio_venta,
        }
        return JsonResponse(data)
    except Productos.DoesNotExist:
        return JsonResponse({'error': 'Producto no encontrado'}, status=404)
    
@csrf_exempt  # Desactiva CSRF para pruebas. Usa un token CSRF válido en producción.
def procesar_seleccion(request):
    if request.method == 'POST':
        try:
            seleccionados = request.POST.getlist('seleccionados[]')
            if not seleccionados:
                return JsonResponse({'error': 'No se seleccionaron productos'}, status=400)
            
            productos = Productos.objects.filter(id_producto__in=seleccionados)
            productos_data = list(productos.values('id_producto', 'nombre', 'cod_producto', 'precio_venta'))
            
            return JsonResponse({'productos': productos_data})
        except Exception as e:
            print(f'Error al procesar selección: {e}')
            return JsonResponse({'error': 'Error interno del servidor'}, status=500)
    
    return JsonResponse({'error': 'Método no permitido'}, status=405)