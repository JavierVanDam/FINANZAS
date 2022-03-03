from django.urls import path
from .views import registracion, login_view, post_login_view

urlpatterns = [
    path('registrar/', registracion, name='registrar'),
    path('login/', login_view, name='login'),
    path('post-login/<int:id>', post_login_view.as_view(), name='post-login')
]
