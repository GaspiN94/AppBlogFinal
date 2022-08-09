# proyectofinal
Proyecto final para curso de Python 

AUTOR : NICOLAS, GASPAR AGUSTIN 

Lamentablemente no realizaron aportes a el trabajo.
-FEDERICO CESTI 
-EMILY FERNANDEZ

Blog 

Recorda iniciar la app en VISUAL STUDIO CODE
-Abrir la terminal
-Hacer migraciones se ejecutan mediante el siguiente comando Python manage.py makemigrations
-Luego Ejecutar Python manage.py migrate para aplicar esos cambios a la base de datos. 
-Y por ultimo correr el servidor  Python manage.py Runserver

Pagina principal: 

http://127.0.0.1:8000/   --- > nos lleva a la pagina de inicio
http://127.0.0.1:8000/pages -----> nos lleva a la lista de post 
http://127.0.0.1:8000/about ---- > informacion del proyecto 

SIN HABER INICIADO SESION:
http://127.0.0.1:8000/accounts/login/ ----> Para iniciar sesion o, si no tenes usuario, registrarte 

Podemos ver todos los post listados y , seleccionar la opcion de ver en detalle 
A la derecha podemos acceder a accesos directos

SI INICIAMOS SESION:
POST 
con la opcion crear post , podemos crear un nuevo poset, llenando todos sus datos.
podemos ver el detalle de cada uno de los post , asi como editarlos y borrarlos.
PERFIL
podemos acceder, con la opcion "Ir a mi perfil" que se encuentra a la derecha, al perfil del usuario. alli vamos a ver todos sus datos y podemos actualizarlos. Solo vamos a poder actualizar la foto si estamos registrados como admin. 
MENSAJES
desde la opcion "Deja tu mensaje" , a la derecha de la pantalla , podremos acceder a la pantalla de mensajes, ver los mensajes de otros usuarios , editar, borrar y dejar un mensaje. 


URL :
PERFIL : http://127.0.0.1:8000/Appblog/perfil/
MENSAJES: http://127.0.0.1:8000/messages/
INICIAR SESION: http://127.0.0.1:8000/accounts/login/
REGISTRARTE: http://127.0.0.1:8000/accounts/register/
CERRAR SESION: http://127.0.0.1:8000/accounts/logout/
CREAR POST: http://127.0.0.1:8000/nuevo/


usuarios: Coderhouse  contraseña: Proyectofinal1
superuser: admin contraseña: admin


Los casos de prueba se encuentran dentro de un excel en el archivo principal. 
Link del video de prueba: 

