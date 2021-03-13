from django.db import models
from apps.mascota.models import Mascota
from apps.usuario.models import Usuario


class Postulante(models.Model):
    id_postulante = models.AutoField(primary_key=True)

    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE, related_name="+", null=True)
    usuario_postulado = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="+", null=True)
    fecha = models.DateTimeField(auto_now=True, null=False)
