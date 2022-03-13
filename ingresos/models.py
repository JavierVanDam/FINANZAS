from django.core import validators
from django.db import models
from cuentas.models import Cuenta
from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator

User = get_user_model()
class CategoriaIngreso(models.Model):
    nombre = models.CharField(max_length=64, unique=True, 
                validators=[MinLengthValidator(limit_value=8, message="VALOR MUY BAJO DE CATEG INGRESO")])
    def __str__(self):
        return self.nombre


class Ingreso(models.Model):
    fecha = models.DateField()
    monto = models.FloatField(validators=[
            MinValueValidator(limit_value=100, message="monto inferior a 100"),
            MaxValueValidator(limit_value=100000, message="monto superior a %(limit_value)")])
    categoria = models.ForeignKey(CategoriaIngreso, related_name="tipo_de_ingreso", on_delete=models.CASCADE, default=1)
    usuario = models.ForeignKey(User, related_name="usuario_carga_ingreso", on_delete=models.CASCADE, default=1)
    fecha_carga = models.DateTimeField(auto_now_add=True)
    #auto_now_add setea ahora/hoy cuando el objeto es creado por primera vez y desp es inmodificable en bbdd
    #auto_now setea ahora/hoy cuando el objeto es creado o updateado, es decir cuando se llama .save()
    def __str__(self):
        return f'{self.fecha} - {self.monto} - {self.usuario}'


#
# {'fecha': '2022-03-24', 'monto': '1', 'categoria': '2', 'usuario': '3'} 'escondidazo': 'chiche', 'csrfmiddlewaretoken': 'rxsfeBtekKCTvXPwJYZlGOqwMeXyGCpsM0UDuTe4xofYCFdrf2yeWXm3ehU3zXNR'}