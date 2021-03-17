from django.db import models
from apps.usuario.models import Usuario
from apps.publicacion.models import Publicacion


class Chat(models.Model):
    id_chat = models.AutoField(primary_key=True)

    publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE, related_name="+", null=True)
    usuario_creador = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="+", null=False)
    usuario_futuro_duenio = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="+", null=False)
    estado = models.BooleanField(null=False)


class Mensaje(models.Model):
    id_mensaje = models.AutoField(primary_key=True)

    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name="+", null=False)
    usuario_emisor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="+", null=False)
    mensaje = models.CharField(max_length=1500, null=True)
    fecha = models.DateTimeField(auto_now=True, null=False)
