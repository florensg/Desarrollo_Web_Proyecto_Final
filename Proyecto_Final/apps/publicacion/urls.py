from django.urls import path
from apps.publicacion import views


urlpatterns = [
    path('crear_publicacion/', views.crear_publicacion, name='crear_publicacion'),
    path('ver_mis_publicaciones/', views.ver_mis_publicaciones, name='ver_mis_publicaciones'),
    path('eliminar_publicacion/', views.eliminar_publicacion, name='eliminar_publicacion'),
    path('confirmar_eliminacion/', views.confirmar_eliminacion, name='confirmar_eliminacion'),
    path('ver_publicaciones/', views.ver_publicaciones_A, name='ver_publicaciones'),
    path('busqueda_filtrada_especie/', views.ver_publicaciones_B, name='busqueda_filtrada_especie'),
]
