from django import forms
from django.core.exceptions import ValidationError
from django.forms import fields
from django.forms.widgets import Widget
from cuentas.models import Cuenta
from django.contrib.auth import get_user_model

User = get_user_model()

from ingresos.models import Ingreso


class formFinal(forms.Form):
    # def __init__(self, *args, **kwargs):
    #     self.request = kwargs.pop('request', None)
    #     super().__init__(*args, **kwargs)
    #     if self.request:
    #         self.usuario = User.objects.get(pk=self.request.user.id)
    #         self.fields['usuario_id'] = forms.ChoiceField(choices= User.objects.all().values_list('id', 'email')
    #                                         if self.usuario.pertenece_a('PUEDE_CARGAR_OTROS_USUARIOS') > 0
    #                                         else User.objects.filter(pk=self.usuario.id).values_list('id', 'email'), widget=forms.Select, initial=self.usuario.id)

    fecha = forms.CharField(widget=forms.TextInput(attrs={'type': 'date'}))  # forms.DateField()
    monto = forms.FloatField()
    categoria_id = forms.ChoiceField(choices=Cuenta.objects.all().values_list('id', 'nombre'), widget=forms.RadioSelect, initial=2, label='CATEG')
    usuario_id = forms.ChoiceField(choices=User.objects.all().values_list('id', 'email'))


class NuevoIngresoFormAbstracto(forms.Form):
    fecha = forms.CharField(widget=forms.TextInput(attrs={'type': 'date'}))  # forms.DateField()
    monto = forms.FloatField()
    categoria = forms.ChoiceField(choices=Cuenta.objects.all().values_list('id', 'nombre'), widget=forms.RadioSelect)


class NuevoIngresoFormSuperCojonudo(NuevoIngresoFormAbstracto):
    usuario = forms.ChoiceField(choices=User.objects.all().values_list('id', 'email'))


class NuevoIngresoFormUsActual(NuevoIngresoFormAbstracto):
    def __init__(self, *args, **kwargs):
        self.id_usuario = kwargs.pop('usuario', None)
        super().__init__(*args, **kwargs)
        # self.fields['usuario'].choices = ((tuple(list(User.objects.filter(pk=3).values('id', 'email'))[0].values())),)
        self.fields['usuario'].choices = User.objects.filter(pk=self.id_usuario).values_list('id', 'email')

    usuario = forms.ChoiceField(disabled=True)


class NuevoIngresoForm2(forms.Form):
    fecha = forms.CharField(widget=forms.TextInput(attrs={'type': 'date'}))
    monto = forms.FloatField()
    categoria = forms.ChoiceField(choices=Cuenta.objects.all().values_list('id', 'nombre'), widget=forms.RadioSelect)
    usuario = forms.ChoiceField(choices=User.objects.all().values_list('id', 'email'))

    #  1. validacion custom de un campo puntual
    # si quiero super customizar una validacion hago una funcion def cleaned_<nombre_field_form>()
    def cleaned_monto(self, *args, **kwargs):
        montoIngresado = self.cleaned_data.get('monto')
        if montoIngresado % 2 == 0:  # par
            raise ValidationError("SOLO SE ADMITEN MONTOS IMPARES")
        return montoIngresado


class ModelFormIngreso(forms.ModelForm):
    fecha = forms.CharField(widget=forms.TextInput(attrs={'type': 'date'}))

    class Meta:
        model = Ingreso
        fields = "__all__"  # ["fecha", "monto", "cate"]

    def clean_monto(self, *args, **kwargs):
        monto = self.cleaned_data.get("monto")
        print("monto es ", monto)
        return monto
