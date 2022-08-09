
from distutils.command.upload import upload
from django.contrib.auth.models import User
from django.db import models
from django.views.generic import ListView, DeleteView, UpdateView, DetailView
from django.views.generic.edit import CreateView
from ckeditor.fields import RichTextField
# Create your models here.


class Post1 (models.Model):
    titulo = models.CharField(max_length=1000)
    subtitulo = models.CharField(max_length=1000)
    introduccion = models.CharField(max_length=4000)
    cuerpo = RichTextField()
    fecha  = models.DateField()
    imagen = models.ImageField(upload_to='fotos', null= True, blank = True)
    autor = models.CharField(max_length=40)


    def __str__(self):
        return self.titulo






