from django.urls import path
from apps.postulante import views


urlpatterns = [
    path('ver_postulantes/<int:publicacion_id>', views.ver_postulantes, name='ver_postulantes'),
    path('confirmar_postulacion/',views.postularse,name='confirmar_postulacion')
]
