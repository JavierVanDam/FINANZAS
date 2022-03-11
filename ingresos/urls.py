from django.urls import path
from .views import procesaNuevoIngreso, procesaNuevoIngreso2, procesaNuevoIngreso3

urlpatterns = [
    path('',procesaNuevoIngreso, name='procesa_nuevo_ingreso'),
    path('_2',procesaNuevoIngreso2, name='procesa_nuevo_ingreso2'),
    path('_3',procesaNuevoIngreso3, name='procesa_nuevo_ingreso3')
]