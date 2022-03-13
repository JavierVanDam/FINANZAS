from django.core.exceptions import ValidationError
from django.shortcuts import render
from .models import Ingreso, CategoriaIngreso
from .forms import *
from django.contrib.auth.models import User
from django.views.generic import View
from funciones_mias import imprimeVarsRequest


class vistaProcesaNuevoIngreso(View):
    def get(self, request, *args, **kwargs):
        # form = formFinal(request=request)
        form = formFinal()
        print(form)
        return render(request, template_name='form_mano_ingresos.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        imprimeVarsRequest(request)
        form = formFinal(request.POST)
        print(form)
        if form.is_valid():
            dictInsercion = form.cleaned_data
            ingNuevo = Ingreso(**dictInsercion)
            print(dictInsercion)
            ingNuevo.save()
            return render(request, template_name='form_mano_ingresos.html')  # , context={'form': form})
        else:
            return render(request, template_name='form_mano_ingresos.html')  # , context={'form': form})


def procesaNuevoIngreso(request):
    status = 'GET POR DEFAULT'

    if request.method == 'POST':
        print(request.POST)
        form = NuevoIngresoFormUsActual(request.POST, usuario=request.user.id)
        print('NuevoIngresoFormUsActual: ', NuevoIngresoFormUsActual)
        if form.is_valid():
            # PUEDO INSTANCIAR Y GUARDAR EL OBJETO XQ EL FORM (NO NECMENTE EL MODELO) ESTAN OK
            # solo en un ModelForm el form esta atado al model, en este caso no implica que el modelo este ok
            status = 'FORM VALIDO BOUNDEADO'
            dictInsercion = form.cleaned_data
            dictInsercion['categoria'] = CategoriaIngreso.objects.get(id=dictInsercion['categoria'])
            dictInsercion['usuario'] = User.objects.get(id=dictInsercion['usuario'])
            ingresoNuevo = Ingreso(**dictInsercion)
            try:
                ingresoNuevo.full_clean()  # esto raisea un error si (https://docs.djangoproject.com/en/1.10/ref/models/instances/#validating-objects):
                # 1. algun campo no pasa una validacion
                # 2. no cumple validacion custom completa del modelo (si eciste, en el metodo clean())
                # 3. no cumple unicidad (unique, en caso q exista)
                ingresoNuevo.save()
                print(f"GUARDASTE CON EXITO: {ingresoNuevo}")
            except ValidationError as e:
                # VUELVO AL FORM ORIGINAL, CON ERRORES
                status = f'FORM BOUNDEADO CON ERRORES: {str(e)}'
                return render(request=request, template_name='form_mano_ingresos.html', context={'form': form, 'status': status})

        else:
            status = "ERROR POST - FORM NO VALIDO"
            return render(request=request, template_name='form_mano_ingresos.html', context={'form': form, 'status': status, 'errores': form.errors})

    # GET, FORM UNBOUND
    if request.user.pertenece_a('PUEDE_CARGAR_OTROS_USUARIOS') > 0:
        print(f'{request.user.email} topisimo')
        form = NuevoIngresoFormSuperCojonudo()
    else:
        print(f'{request.user.email} no tiene permisos cojonudos')
        form = NuevoIngresoFormUsActual(usuario=request.user.id)

    return render(request=request, template_name='form_mano_ingresos.html', context={'form': form, 'status': status})
