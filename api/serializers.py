import imp
from rest_framework import serializers
from cuentas.models import Cuenta
from ingresos.models import *


class CuentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuenta
        fields = ['id', 'nombre']

class CategoriaIngresoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaIngreso
        fields = '__all__'
