from django.urls import path
from apps.usuario import views


urlpatterns = [
    path('ver_perfil/', views.ver_perfil, name='ver_perfil'),
    path('editar_perfil/', views.editar_perfil, name='editar_perfil'),
    path('ver_usuario_externo/', views.ver_usuario_externo, name='ver_usuario_externo')
]
