from django.core.exceptions import ValidationError
from django.shortcuts import render
from .models import Ingreso, CategoriaIngreso
from .forms import NuevoIngresoForm, NuevoIngresoForm2, ModelFormIngreso
from django.contrib.auth.models import User


def procesaNuevoIngreso(request):
    status = 'GET POR DEFAULT'
    form = NuevoIngresoForm()
    if request.method == 'POST':
        form = NuevoIngresoForm(request.POST)
        if form.is_valid(): 
            #PUEDO INSTANCIAR Y GUARDAR EL OBJETO XQ EL FORM (NO NECMENTE EL MODELO) ESTAN OK
            #solo en un ModelForm el form esta atado al model, en este caso no implica que el modelo este ok
            status = 'FORM VALIDO BOUNDEADO'
            dictInsercion = form.cleaned_data
            dictInsercion['categoria'] = CategoriaIngreso.objects.get(id=dictInsercion['categoria'])
            dictInsercion['usuario'] = User.objects.get(id=dictInsercion['usuario'])
            ingresoNuevo = Ingreso(**dictInsercion)
            try:
                ingresoNuevo.full_clean()   #esto raisea un error si (https://docs.djangoproject.com/en/1.10/ref/models/instances/#validating-objects):
                                            # 1. algun campo no pasa una validacion
                                            # 2. no cumple validacion custom completa del modelo (si eciste, en el metodo clean())
                                            # 3. no cumple unicidad (unique, en caso q exista)
                ingresoNuevo.save()
                print(f"GUARDASTE CON EXITO: {ingresoNuevo}")
            except ValidationError as e:
                #VUELVO AL FORM ORIGINAL, CON ERRORES
                status = f'FORM BOUNDEADO CON ERRORES: {str(e)}'
                

        #FORM BOUNDEADO, CON ALGO SE LLENO PORQUE ESTAMOS EN EL POST
        
    #GET, FORM UNBOUND
    return render(request=request, template_name='form_mano_ingresos.html', context={'form':form, 'status':status})




def procesaNuevoIngreso2(request):
    form = NuevoIngresoForm2(request.POST or None)
    errores = ''
    if form.is_valid():
        print(form.cleaned_data) #diccionario con la data ok
        fechaPost = form.cleaned_data.get("fecha")
        montoPost = form.cleaned_data.get("monto")
        categoriaPost = form.cleaned_data.get("categoria")        
        usuarioPost = form.cleaned_data.get("usuario")
        ingresoNuevo = Ingreso(fecha=fechaPost, monto=montoPost, 
                        categoria=CategoriaIngreso.objects.get(id=categoriaPost),
                        usuario=User.objects.get(id=usuarioPost))
        try:
            ingresoNuevo.full_clean()
            ingresoNuevo.save()
            print(f"GUARDASTE CON EXITO: {ingresoNuevo}")
        except ValidationError as e:
            #VUELVO AL FORM ORIGINAL, CON ERRORES
            errores = str(e)
  
    return render(request=request, template_name='form_mano_ingresos.html', context={'form':form, 'errores':errores})


def procesaNuevoIngreso3(request):
    form = ModelFormIngreso(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request=request, template_name='form_mano_ingresos.html', context={'form':form})