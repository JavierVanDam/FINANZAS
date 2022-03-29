from django.urls import path
from .views import vistaProcesaNuevoIngreso, CreaCategoria, ListadoIngresos

urlpatterns = [
    path('', vistaProcesaNuevoIngreso.as_view(), name='procesa_nuevo_ingreso'),
    # path('',procesaNuevoIngreso, name='procesa_nuevo_ingreso'),
    path('nueva-categ', CreaCategoria.as_view()),
    path('listado-ingresos', ListadoIngresos.as_view()),

]
