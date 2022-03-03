from django.urls import path, include
from .views import CreaCuenta, ListaCuentas, DetalleCuenta, nuevaCuentaForm

app_name = 'cuentas'


urlpatterns = [
    path("nueva/", CreaCuenta.as_view(), name="crea_cuenta"),
    path("nueva_form/", nuevaCuentaForm, name="crea_cuenta_form"),
    path("listado_cuentas/", ListaCuentas.as_view(), name="lista_cuentas"),
    path("detalle/<int:pk>", DetalleCuenta.as_view(), name="detalle_cuenta"),
]
