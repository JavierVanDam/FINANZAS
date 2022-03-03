from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import Usuario



User = get_user_model()


class RegisterForm(forms.ModelForm):
    #password y password_2 son campos q SE AGREGAN a los definidos en Meta/model/fields
    password = forms.CharField(widget=forms.PasswordInput)
    password_2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        # exclude = ['last_login', 'is_superuser', 'is_admin', 'is_active', 'date_joined', 'groups', 'user_permissions']
        fields = ['email', 'nombre', 'apellido', 'domicilio', 'telefono']

    #VALIDACION MONO
    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("email is taken")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_2 = cleaned_data.get("password_2")
        if password is not None and password != password_2:
            self.add_error("password_2", "Your passwords must match")
        return cleaned_data

class UserLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())



class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = Usuario
        fields = '__all__'


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = Usuario
        # fields = ('email',)
        fields = '__all__'