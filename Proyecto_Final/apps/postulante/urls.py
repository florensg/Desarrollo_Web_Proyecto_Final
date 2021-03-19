from django.urls import path
from apps.postulante import views


urlpatterns = [
    path('ver_postulantes/<int:publicacion_id>', views.ver_postulantes, name='ver_postulantes'),
    path('ver_mis_postulaciones/',views.ver_mis_postulaciones, name='ver_mis_postulaciones'),
    path('elegir_duenio/<int:id_publicacion>', views.elegir_duenio, name='elegir_duenio'),
    path('hacer_duenio/', views.hacer_duenio, name='hacer_duenio'),
]
