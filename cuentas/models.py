from django.db import models

TIPOS_CUENTA = (('INGRESOS', 'INGRESOS'), ('GASTOS', 'GASTOS'), ('AMBOS', 'AMBOS'))


class Cuenta(models.Model):
    nombre = models.CharField(max_length=64)
    tipo_cuenta = models.CharField(max_length=64, choices=TIPOS_CUENTA)
    permite_cuotas = models.BooleanField(default=False)

    def __str__(self):
        return "{}".format(self.nombre)

