from django.urls import path
from apps.usuario import views


urlpatterns = [
    path('ver_perfil/', views.ver_perfil, name='ver_perfil'),
    path('editar_perfil/<int:usuario_id>', views.editar_perfil, name='editar_perfil'),
    path('ver_usuario_externo/<int:usuario_id>', views.ver_usuario_externo, name='ver_usuario_externo'),
    path('calificar_usuario/', views.calificar_usuario, name='calificar_usuario'),
]
