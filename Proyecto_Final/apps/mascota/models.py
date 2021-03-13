from django.db import models
from apps.publicacion.models import Publicacion
from apps.usuario.models import Usuario


class Mascota(models.Model):
    id_mascota = models.AutoField(primary_key=True)

    publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE, related_name="+", null=True)
    foto = models.ImageField(upload_to='media', null=False)
    sexo = models.CharField(max_length=6, blank=True, null=False, choices=(('macho', 'Macho'),
                                                                           ('hembra', 'Hembra')))
    raza = models.CharField(max_length=50, null=True)
    edad = models.PositiveIntegerField(null=False)
    descripcion = models.CharField(max_length=500, null=False)
    usuario_futuro_duenio = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="+", null=True)
    estado = models.BooleanField(null=True)
