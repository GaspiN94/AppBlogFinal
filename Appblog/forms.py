from cgi import print_arguments
from pyexpat import model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms 
from ckeditor.fields import RichTextField




class formulariopost (forms.Form):
    titulo = forms.CharField(max_length=1000)
    subtitulo = forms.CharField(max_length=1000)
    introduccion = forms.CharField(max_length=4000)
    cuerpo = forms.CharField()
    fecha  = forms.DateField()
    imagen = forms.ImageField()
