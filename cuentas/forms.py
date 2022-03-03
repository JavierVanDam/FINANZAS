from django import forms
from django.db import models
from django.forms import fields
from django.core.exceptions import ValidationError

from .models import Cuenta, TIPOS_CUENTA


class CuentaForm(forms.ModelForm):
    class Meta:
        model = Cuenta
        fields = '__all__'


class FormularioNuevaCuenta(forms.Form):
    nombre = forms.CharField()
    # CONVIENE PONER EL MISMO NOMBRE DEL FORM/INPUT HTML AL DEL CAMPO DEL MODELO, PARA Q
    # LUEGO PUEDAS INVOCAR MODELO.SAVE() Y COINCIDAN LOS CAMPOS DEL MODELO CON EL DEL FORM/INPUT
    tipo_cuenta = forms.ChoiceField(choices=TIPOS_CUENTA, required=True)
    permite_cuotas = forms.BooleanField(required=False)

    # VALIDACION CUSTOM MONOCAMPO
    def clean_nombre(self, *args, **kwargs):
        nombre = self.cleaned_data.get('nombre')
        if len(nombre) < 5:
            raise forms.ValidationError('NOMBR CUENTA DEBE TENER MAS CARACTERES')
        return nombre

    # VALIDACION CUSTOM MULTICAMPO
    def clean(self):
        cleaned_data = super().clean()
        nombre = cleaned_data.get("nombre")
        permite_cuotas = cleaned_data.get("permite_cuotas")

        if nombre.upper().startswith(('A','E','I','U','O')) and permite_cuotas==True:
            print("esoty en clean")
            raise ValidationError(f'NOMBRE NO PUEDE EMPEZAR CON VOCAL (EN ESTE CASO EMPIEZA CON {nombre[0]}) SI PERMITE CUOTAS')