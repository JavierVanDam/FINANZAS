from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.views.generic.base import TemplateView
from django.urls import reverse
from django.contrib.auth import get_user_model

from .forms import RegisterForm, UserLoginForm

User = get_user_model()


def registracion(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            print('form valido, la cleaned_data es ', form.cleaned_data)
            form.cleaned_data.pop('password_2')
            print('post elim de pass_w, la cleaned_data es ', form.cleaned_data)

            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user_nuevo = User.objects.create_user(**form.cleaned_data)

            return render(request, 'usuarios/registracion.html', {'usuario': user_nuevo})
        else:
            print('form invalido: ', form)
            print('los errores son: ', form.errors)
            return render(request, 'usuarios/registracion.html', {'form': form})
    else:  # GET DE LA URL, PRIMERA VEZ. PRESENTO EL FORM VACIO
        form = RegisterForm()
        context = {'form': form}
        print("estoy en registracion, contexto: ", context)
        return render(request, 'usuarios/registracion.html', context)


def login_view(request):
    print('en login')
    if request.method == 'POST':
        print('en post')
        form = UserLoginForm(request.POST)
        if form.is_valid():
            print('form valido')
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user:
                print('login exitoso: ', user)
                if user.is_active:
                    login(request, user)
                    # !!fundamental https://stackoverflow.com/questions/13136057/django-if-user-is-authenticated-not-working
                    return redirect('post-login', id=user.id)
                print("usuario no activo")
            else:
                print('usuario contraseña no valido')
                return render(request, 'usuarios/login.html', {'form': form, 'errores': 'error de autenticación, ingrese us/pass nuevamente'})
        else:
            print('no se pudo autenticar')
    form = UserLoginForm()
    return render(request, 'usuarios/login.html', {'form': form})


class post_login_view(TemplateView):
    template_name = 'usuarios/post_login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # tomo el parametro de la url
        idUsuario = self.kwargs['id']  # este es el param de la url. pero tenes q agreagrle el self en una CBV
        # traigo el objeto usuario segun el id
        # usuario = User.objects.get(pk=idUsuario)
        usuario = get_object_or_404(User, pk=idUsuario)
        # agrego ese objeto al contexto
        context['usuario'] = usuario
        return context
