import imp
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='base.html')),
    path('admin/', admin.site.urls),
    path('usuario/', include('usuarios.urls')),
    path('cuentas/', include('cuentas.urls')),
]
