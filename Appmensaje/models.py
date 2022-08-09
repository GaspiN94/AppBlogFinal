from re import M
from django.db import models

# Create your models here.
class Mensaje (models.Model):
    autor = models.CharField(max_length=40)
    mensaje = models.CharField(max_length=1000)
    