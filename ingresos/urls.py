from django.urls import path
from .views import vistaProcesaNuevoIngreso, CreaCategoria, ListadoIngresos, DetalleIngreso

app_name = 'ingresos'

urlpatterns = [
    path('', vistaProcesaNuevoIngreso.as_view(), name='procesa_nuevo_ingreso'),
    # path('',procesaNuevoIngreso, name='procesa_nuevo_ingreso'),
    path('nueva-categ', CreaCategoria.as_view(), name='nueva-categ'),
    path('listado-ingresos', ListadoIngresos.as_view() , name='lista-ingresos'),
    path('detalle/<int:pk>', DetalleIngreso.as_view() , name='detalle-ingreso'),

]
