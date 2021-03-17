from django.urls import path
from apps.publicacion import views


urlpatterns = [
    path('crear_publicacion/', views.crear_publicacion, name='crear_publicacion'),
    path('ver_mis_publicaciones/', views.ver_mis_publicaciones, name='ver_mis_publicaciones'),
    path('editar_publicacion/<int:publicacion_id>', views.editar_publicacion, name='editar_publicacion'),
    path('eliminar_publicacion/<int:publicacion_id>', views.eliminar_publicacion, name='eliminar_publicacion'),
    path('confirmar_eliminacion/<int:publicacion_id>', views.confirmar_eliminacion, name='confirmar_eliminacion'),
    path('ver_publicaciones/', views.ver_publicaciones_A, name='ver_publicaciones'),
    path('busqueda_filtrada_especie/', views.ver_publicaciones_B, name='busqueda_filtrada_especie'),
    path('ver_publicacion_usuario_externo/<int:usuario_id>',views.ver_publicacion_usuario_externo, name='ver_publicacion_usuario_externo')
]
