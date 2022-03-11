from django import forms
from django.core.exceptions import ValidationError
from django.forms import fields
from django.forms.widgets import Widget
from cuentas.models import Cuenta
from django.contrib.auth.models import User


from ingresos.models import Ingreso


class NuevoIngresoForm(forms.Form):
    fecha = forms.CharField(widget=forms.TextInput( attrs={'type':'date'})) #forms.DateField()
    monto = forms.FloatField()
    categoria = forms.ChoiceField(choices=Cuenta.objects.all().values_list('id', 'nombre'), widget=forms.RadioSelect)
    usuario = forms.ChoiceField(choices=User.objects.all().values_list('id', 'username'))
    



class NuevoIngresoForm2(forms.Form):
    fecha = forms.CharField(widget=forms.TextInput( attrs={'type':'date'})) 
    monto = forms.FloatField()
    categoria = forms.ChoiceField(choices=Cuenta.objects.all().values_list('id', 'nombre'), widget=forms.RadioSelect)
    usuario = forms.ChoiceField(choices=User.objects.all().values_list('id', 'username'))

    #  1. validacion custom de un campo puntual
    #si quiero super customizar una validacion hago una funcion def cleaned_<nombre_field_form>()
    def cleaned_monto(self, *args, **kwargs):
        montoIngresado = self.cleaned_data.get('monto')
        if montoIngresado % 2 == 0: #par
            raise ValidationError("SOLO SE ADMITEN MONTOS IMPARES")
        return montoIngresado


class ModelFormIngreso(forms.ModelForm):
    fecha = forms.CharField(widget=forms.TextInput( attrs={'type':'date'})) 
    class Meta:
        model = Ingreso
        fields = "__all__" #["fecha", "monto", "cate"]
    
    def clean_monto(self, *args, **kwargs):
        monto = self.cleaned_data.get("monto")
        print("monto es ", monto)
        return monto
