# django desde 0
para iniciar nuestro proyecto debemos tener instalado python y virtualenv (virtualenv viene con python3.*)
creamos una nueva carpeta con el nombre de nuestro nuevo proyecto.
abrimos una terminal dentro de la carpeta y escribimos el comando
~~~
$ python3 -m venv [nombre del proyecto]
~~~
se genera una nueva carpeta en la cual se van a almacenar nuestros datos del entorno virtual.
a continuacion requerimos activar el entorno virtual
~~~
$ source [nombre del entorno virtual/bin/activate]
~~~
una vez dentro del entorno virtual procedemos a instalar django (importante: se instla dentro del entorno virtual, no por fuera)
~~~
(entorno_virtual)$ pip install django
~~~
ahora vamos a crear nuestro proyecto
~~~
(entorno_virtual)$ django-admin startproject [nombre del proyecto]
~~~
se creará una carpeta nueva con el nombre que le diste, nos movemos dentro de la carpeta nueva
~~~
(entorno_virtual)$ cd [nombre de la carpeta]
~~~
una vez aqui adentro nos encontraremos con un archivo llamado manage.py, con este archivo haremos de todo con nuestro proyecto. Podemos crear nuevas aplicaciones para nuestro proyecto.
crearemos nuestro primer modulo con el comando
~~~
$ ./manage.py startapp [nombre_de_la_app]~~~
comando
~~~
$ ./manage.py check
~~~
revisa los cambios realizados

~~~
@admin.register(NombreDelModelo)
~~~

es un decorador y nos permite usarlo en vez del admin.site.register para mostrar mas datos en la pantalla del admin.

En Django 1.9 en adelante, para las vistas basadas en clase, se debe de utilizar el LoginRequiredMixin, el cual hay que importarlo desde: django.contrib.auth.mixins. y luego ese mixin se pasa a la vita basada en clase asi:  ProductView(LoginRequiredMixin, CreateView).



Hay que tener en cuenta que en settings.py debe de estar la variable LOGIN_URL = '/' para que al detectar de que el usuario no esta logueado, lo mande a la página de login.



Este mixinno debe ser creado, ya que hace parte de los mixins de django 1.9+, a no ser de que quieran usar uno propio para que hagaalgo diferente.
