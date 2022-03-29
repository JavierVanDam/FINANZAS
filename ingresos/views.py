from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect, reverse
from .models import Ingreso, CategoriaIngreso
from .forms import *
from django.contrib.auth.models import User
from django.views.generic import View, ListView
from django.views.generic.edit import CreateView

from funciones_mias import imprimeVarsRequest

class ListadoIngresos(ListView):
    model = Ingreso

class CreaCategoria(CreateView):
    model = CategoriaIngreso
    fields = '__all__'
    def get_success_url(self):
        return reverse('procesa_nuevo_ingreso')



class vistaProcesaNuevoIngreso(View):
    def get(self, request, *args, **kwargs):
        form = formFinal(request=request)
        # form = formFinal()
        return render(request, template_name='form_mano_ingresos.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        form = formFinal(request.POST, request=request)
        if form.is_valid():
            dictInsercion = form.cleaned_data
            ingNuevo = Ingreso(**dictInsercion)
            print(dictInsercion)
            ingNuevo.save()
            return render(request, template_name='form_mano_ingresos.html')  # , context={'form': form})
        else:
            return render(request, template_name='form_mano_ingresos.html')  # , context={'form': form})

