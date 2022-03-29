from django.contrib.auth import get_user_model
User = get_user_model()
u = User.objects.get(pk=3)
from ingresos.models import Ingreso, CategoriaIngreso

datos = {'fecha': '2022-03-23', 'monto': 12.0, 'categoria': '2', 'usuario': '4'}
ing = Ingreso(**datos)
ing.save()

datos = {'fecha': '2022-03-23', 'monto': 12.0, 'categoria': CategoriaIngreso.objects.get(pk=2), 'usuario':  User.objects.get(pk=4)}
ing = Ingreso(**datos)
ing.save()
