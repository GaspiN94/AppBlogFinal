from django.db import models
from django.contrib.auth.models import User, AbstractUser

# Create your models here.

class Avatar (models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE )
    imagen = models.ImageField(upload_to ='avatares/', null = True, blank = True)
    def __str__(self):
        return self.user

class Usuario (models.Model):
    user = models.ForeignKey(User, null= True, on_delete= models.CASCADE)
    link = models.URLField(max_length=100)
    descripcion = models.CharField(max_length=1000)

    def __str__(self):
        return self.user

