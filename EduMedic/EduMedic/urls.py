"""
URL configuration for EduMedic project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from sitio import views

urlpatterns = [
  path('admin/', admin.site.urls),
  path('', views.Boot,name='Comienzo'),
  path('inicio/', views.Principal,name='Inicio'),
  path('rv/',views.RV,name='RV'),
  path('cortes/',views.Cortes,name='Cortes'),
  path('ayuda/',views.Ayuda,name='Ayuda'),
  path('sistemas/',views.Sistemas,name='Sistemas'),
  path('sisA/',views.SIstemaA,name='sisA'),
  path('sisB/',views.SIstemaB,name='sisB'),
  path('sisC/',views.SIstemaC,name='sisC'),
  path('medicamentos/',views.Medicamentos,name='Medicamentos'),
  path('notas/nueva',views.CrearNota, name="CrearNota"),
  path('login/',views.Login,name='Login'),
  path('validarLogin/',views.validarLogin,name='validarLogin'),
  path('login#errorNA',views.Login,name="NoUser"),
  path('login#errorPass',views.Login,name="NoPass"),
  path('login#newUser',views.Login,name="SignupYes"),
  path('notas/', views.Notas,name='Notas'),
  path('notas/creando', views.NotaNueva, name="NuevaNota"),
  path('eliminarNota/<int:id>/',views.EliminarNota,name='EliminarNota'),
  path('editarNota/<int:id>',views.EditorDeNotas,name='EditorNotas'),
  path('notaConfirmada/<int:id>',views.NotaEditada,name='EditarNota'),
  path('signup/',views.Signup,name='Signup'),
  path('creandoUser',views.NuevoUser,name='CrearUser'),
  path('perfil/',views.Perfil,name='Perfil'),
  path('pfpNew/',views.cambioImagen,name='UpdatePFP'),
  path('libros/',views.Libros,name="Libros"),
  path('librosAdmin/',views.LibrosAdmin,name="LibrosAdmin"),
  path('aprobarLibro/<int:id>',views.AprobarLibro,name='Aprobar'),
  path('quitarLibro/<int:id>',views.QuitarLibro,name='Quitar'),
  path('NoAprobado/',views.LibrosNoAprobados,name='NoAprobados'),
  path('agregarLibro/',views.AgregarLibroV,name="AgregarLibro"),
  path('nuevoLibro',views.NuevoLibro,name='NuevoLibro'),
  path('aboutUs', views.AboutUs,name='AboutUs')
] 

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)