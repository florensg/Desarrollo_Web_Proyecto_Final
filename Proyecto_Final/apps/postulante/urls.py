from django.urls import path
from apps.postulante import views


urlpatterns = [
    path('ver_postulantes/<int:publicacion_id>', views.ver_postulantes, name='ver_postulantes'),
    path('ver_mis_postulaciones/',views.ver_mis_postulaciones, name='ver_mis_postulaciones')
]
