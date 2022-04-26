from django.urls import path, include
from .views import *

app_name = 'api'


urlpatterns = [
    path("lista-cuentas/", ListaCuentasJson.as_view(), name="lista-cuentas"),
    path("lista-cuentas-funcion/", devuelveListadoCuentasFuncion, name="lista-cuentas-funcion"),
    path("lista-categoria-ingreso/", ListaCategoriasIngresosJson.as_view(), name="lista-categoria-ingreso"),
    
]
