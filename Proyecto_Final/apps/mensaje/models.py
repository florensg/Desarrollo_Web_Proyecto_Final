from django.db import models
from apps.mascota.models import Mascota
from apps.usuario.models import Usuario


class Chat(models.Model):
    id_chat = models.AutoField(primary_key=True)

    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE, related_name="+", null=False)
    usuario_creador = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="+", null=False)
    usuario_futuro_duenio = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="+", null=False)
    estado = models.BooleanField(null=False)


class Mensaje(models.Model):
    id_mensaje = models.AutoField(primary_key=True)

    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name="+", null=False)
    usuario_emisor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="+", null=False)
    mensaje = models.CharField(max_length=1500, null=True)
    fecha = models.DateTimeField(auto_now=True, null=False)
