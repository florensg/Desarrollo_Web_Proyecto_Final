from django.db import models
from apps.publicacion.models import Publicacion
from apps.usuario.models import Usuario


class Postulante(models.Model):
    id_postulante = models.AutoField(primary_key=True)

    publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE, related_name="+", null=True)
    usuario_postulado = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="+", null=True)
    fecha = models.DateTimeField(auto_now=True, null=False)
