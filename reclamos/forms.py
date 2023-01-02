from django.forms import ModelForm
from .models import Reclamo, Respuesta
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ConsultaForm(ModelForm):
    class Meta:
        model=Reclamo
        fields=['nombre','apellido','dni', 'carrera','registro', 'categoria', 'email', 'telefono', 'consulta']


class RespuestaForm(ModelForm):
    class Meta:
        model=Respuesta
        fields=['respuesta',]


class CreateUserForm(UserCreationForm):
    class Meta:
        model= User
        fields =['username', 'email', 'password1', 'password2']

