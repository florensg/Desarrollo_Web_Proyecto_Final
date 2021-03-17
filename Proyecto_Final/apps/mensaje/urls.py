from django.urls import path
from apps.mensaje import views


urlpatterns = [
    path('enviar_correo/', views.enviar_correo, name='enviar_correo'),
    path('gracias/', views.gracias, name='gracias'),

    path('lista_de_chats/', views.lista_de_chats, name='lista_de_chats'),
    path('chat/<int:id_chat>', views.chat, name='chat'),
    path('enviar_mensaje/<int:id_chat>', views.enviar_mensaje, name='enviar_mensaje'),
]
