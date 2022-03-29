from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class Usuario(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(default=timezone.now)

    #nombre
    nombre = models.CharField(max_length=128)
    apellido = models.CharField(max_length=128)

    #AGREGADO POST
    domicilio = models.CharField(max_length=255, blank=True)
    telefono = models.CharField(max_length=32, blank=True)



    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def pertenece_a(self, nombre_grupo):
        return self.groups.filter(name=nombre_grupo).count()

    def __str__(self):
        return self.email





