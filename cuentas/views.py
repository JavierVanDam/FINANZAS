from django.views.generic import CreateView, ListView, DetailView
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import Cuenta
from django.urls import reverse_lazy
from .forms import FormularioNuevaCuenta
from django.shortcuts import render
#ALTERNATIVA 1. CLASS BASED VIEW CREATE CUENTA


class CreaCuenta(PermissionRequiredMixin, CreateView):
    permission_required = 'cuentas.add_cuenta'
    model = Cuenta
    fields = '__all__'
    success_url = reverse_lazy('cuentas:lista_cuentas') #'http://127.0.0.1:8000/base/'

class ListaCuentas(ListView):
    model = Cuenta


class DetalleCuenta(DetailView):
    model = Cuenta


#ALTERNATIVA 2. FULL CUSTOMIZADA CREATE CUENTA. CUSTOMIZO LA VIEW Y EL FORM
@login_required(login_url='login')
@permission_required('cuentas.add_cuenta', raise_exception=True)
def nuevaCuentaForm(request):
    form = FormularioNuevaCuenta(request.POST or None)
    if form.is_valid():
        print("FORM VALIDO: ", form.cleaned_data)
        cuentaNueva = Cuenta(**form.cleaned_data)
        cuentaNueva.save()
        return redirect('lista_cuentas')
    else:
        #CUANDO HAY ERRORES EN EL FORM, DJANGO SE ENCARGA AUTOMATICAMENTE DE PONERLO EN EL FORM
        # DEBAJO DEL CAMPO Q CORRESPONDA
        print("FORM ERRORES: ", form.errors)



    return render(request, template_name='cuentas/cuenta_form_a_mano.html', context={'form':form})
