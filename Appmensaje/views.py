from django.shortcuts import render
from django.http import HttpResponse
from Appmensaje.models import *
from django.template import loader
from django.views.generic import ListView, DeleteView, UpdateView, DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy


from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class Listmensaje (ListView):
    model = Mensaje
    template_name = "Appblog/mensaje_list.html"


class Createmensaje(LoginRequiredMixin, CreateView):
    model = Mensaje
    success_url = "/Appmensajes/mensajes"
    fields = ['autor', 'mensaje']

class Updatemensaje (LoginRequiredMixin, UpdateView):
    model = Mensaje
    success_url = "/Appmensajes/mensajes"
    fields = ['autor', 'mensaje']

class Deletemensaje (LoginRequiredMixin, DeleteView):
    model = Mensaje
    success_url = "/Appmensajes/mensajes"