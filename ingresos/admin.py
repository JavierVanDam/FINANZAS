from django.contrib import admin
from .models import Ingreso, CategoriaIngreso

@admin.register(Ingreso)
class IngresoAdmin(admin.ModelAdmin):
    pass



@admin.register(CategoriaIngreso)
class CategoriaIngresoAdmin(admin.ModelAdmin):
    pass

