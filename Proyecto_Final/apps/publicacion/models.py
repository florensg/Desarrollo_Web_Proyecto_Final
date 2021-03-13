from django.db import models
from apps.usuario.models import Usuario


class Publicacion(models.Model):
    id_publicacion = models.AutoField(primary_key=True)

    usuario_creador = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="+", null=True)
    foto = models.ImageField(upload_to='media', null=False)
    fecha = models.DateTimeField(auto_now=True, null=False)
    descripcion = models.CharField(max_length=500, null=True)
    especie = models.CharField(max_length=5, blank=True, null=False, choices=(('perro', 'Perro'),
                                                                              ('gato', 'Gato')))
    cantidad_de_mascotas = models.PositiveIntegerField(null=True)
    estado = models.BooleanField(null=False)


class Contador(models.Model):
    id_contador = models.AutoField(primary_key=True)

    publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE, related_name="+", null=True)
    i = models.PositiveIntegerField(null=False)
