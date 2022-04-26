from rest_framework import generics
from cuentas.models import Cuenta
from ingresos.models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from time import sleep
from django.http import HttpResponseBadRequest
# FBVs


@api_view(['GET'])
def devuelveListadoCuentasFuncion(request):
    if request.method == 'GET':
        sleep(1)
        todasCuentas = Cuenta.objects.all()
        cuentasSerializadas = CuentaSerializer(todasCuentas, many=True)
        # tenes q poner many=True xq el serializer espera un modelo, y le estas pasando un queryset
        # asi q le aclaras q le estas pasando una LISTA de modelos

        return Response(cuentasSerializadas.data)
        # return HttpResponseBadRequest('invalid request')


# CBVs

class ListaCuentasJson(generics.ListCreateAPIView):
    queryset = Cuenta.objects.all()
    serializer_class = CuentaSerializer


class ListaCategoriasIngresosJson(generics.ListCreateAPIView):
    queryset = CategoriaIngreso.objects.all()
    serializer_class = CategoriaIngresoSerializer
