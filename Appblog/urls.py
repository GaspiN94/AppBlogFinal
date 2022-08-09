from ast import Index
from django.urls import path, URLPattern
from Appblog.views import  * 
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('perfil/', perfil, name= 'perfil'),
    path('login/', login_request, name= 'Login'),
    path('register/', register, name = 'Register'),
    path('logout/', LogoutView.as_view (template_name= 'Appblog/logout.html'), name ='Logout' ),

    path('<pk>/', Detailpost.as_view(), name = 'Detail'), 
    path('editar/<pk>', Updatepost.as_view(), name= 'Edit'),
    path('borrar/<pk>', Deletepost.as_view(), name = 'Delete'),
    path('about', about, name = 'about')


   
  
]