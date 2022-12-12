from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns


urlpatterns = [
    # ---- Urls principales ---- #
    path('', views.Principal, name='index'),
    path('inicio', views.Principal, name='inicio'),
    path('about', views.about, name='about'),
    path('mision', views.mision, name='mision'),
    path('vision', views.vision, name='vision'),
    path('galeria', views.galeria, name='galeria'),
    path('contacto', views.galeria, name='contacto'),
    # ---- Urls Categorias ---- #
    path('listarCategoria', views.listarCategoria, name = 'listarCategoria'),
    path('crearCategoria', views.crearCategoria, name='crearCategoria'),
    path('eliminarCategoria/<int:id>', views.eliminarCategoria, name='eliminarCategoria'),
    path('editarCategoria/<int:id>', views.editarCategoria, name='editarCategoria'),
    # ---- Urls Noticias ---- #
    path('listarNoticias', views.listarNoticias, name = 'listarNoticias'),
    #path('crearNoticia', views.crearNoticia, name='crearNoticia'),
    path('crear-noticia', views.CrearNoticia.as_view(), name='crear-noticia'),
    path('eliminarNoticia/<int:id>', views.eliminarNoticia, name='eliminarNoticia'),
    path('editarNoticia/<int:id>', views.editarNoticia, name='editarNoticia'),
    # ---- Urls Comentarios ---- #
    # como sería acá? ................
    # ---- Urls Personas ---- #
    path('crearPersona', views.crearPersona, name='crearPersona'),
    path('listaPersonas', views.listaPersonas, name='listaPersonas'),
    # ---- Urls Sesión ---- #
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
