from django.urls import path
from .views import registracion, login_view, post_login_view, logout_view

app_name = 'usuarios'

urlpatterns = [
    path('registrar/', registracion, name='registrar'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('post-login/<int:id>', post_login_view.as_view(), name='post-login')
]
