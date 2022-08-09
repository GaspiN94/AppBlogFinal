from ast import Index
from django.urls import path, URLPattern
from Appmensaje.views import  * 
from django.contrib.auth.views import LogoutView


urlpatterns = [

    path('mensajes/' , Listmensaje.as_view(), name = 'mensajes'),
    path('nuevo/', Createmensaje.as_view(), name='nuevocomentario'), 
   
    path('editar/<pk>', Updatemensaje.as_view(), name= 'editarcomentario'),
    path('borrar/<pk>', Deletemensaje.as_view(), name = 'borrarcomentario'),
]
