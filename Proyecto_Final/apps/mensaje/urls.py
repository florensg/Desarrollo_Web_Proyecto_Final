from django.urls import path
from apps.mensaje import views

urlpatterns = [
    path('enviar_correo/', views.enviar_correo, name='enviar_correo'),
    path('gracias/', views.gracias, name='gracias'),
]