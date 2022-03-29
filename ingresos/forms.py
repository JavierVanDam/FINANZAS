from django import forms
from django.core.exceptions import ValidationError
from django.forms import fields
from django.forms.widgets import Widget
from .models import CategoriaIngreso
from django.contrib.auth import get_user_model

User = get_user_model()

from ingresos.models import Ingreso


class formFinal(forms.Form):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)
        # if self.request.method == 'GET':
        self.usuario = User.objects.get(pk=self.request.user.id)
        self.fields['usuario_id'] = forms.ChoiceField(choices= User.objects.all().values_list('id', 'email')
                                        if self.usuario.pertenece_a('PUEDE_CARGAR_OTROS_USUARIOS') > 0
                                        else User.objects.filter(pk=self.usuario.id).values_list('id', 'email'), widget=forms.Select, initial=self.usuario.id)

    fecha = forms.CharField(widget=forms.TextInput(attrs={'type': 'date'}))  # forms.DateField()
    monto = forms.FloatField()
    categoria_id = forms.ChoiceField(choices=CategoriaIngreso.objects.all().values_list('id', 'nombre'), widget=forms.RadioSelect(attrs={'class': "categorias_ingreso"}), initial=2, label='CATEG' )
