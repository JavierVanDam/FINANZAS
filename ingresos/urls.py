from django.urls import path
from .views import procesaNuevoIngreso, vistaProcesaNuevoIngreso

urlpatterns = [
    # path('',vistaProcesaNuevoIngreso.as_view(), name='procesa_nuevo_ingreso'),
    path('',procesaNuevoIngreso, name='procesa_nuevo_ingreso'),

]