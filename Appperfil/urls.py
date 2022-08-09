from ast import Index
from django.urls import path, URLPattern
from Appperfil.views import  * 
from Appblog.views import * 

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('actualizarusuario/', actualizar_usuario , name= 'actualizar'),
    path('cargarimagen/', cargar_imagen, name= 'cargarimagen'),
    path('informacion/', actualizar_informacion, name= 'informacion'),
    path('infoadicional/', informacion, name='infoadicional'),



   
  
]