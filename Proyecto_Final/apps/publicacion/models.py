from django.db import models
from apps.usuario.models import Usuario


class Publicacion(models.Model):
    id_publicacion = models.AutoField(primary_key=True)

    usuario_creador = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="+", null=True)
    nombre = models.CharField(max_length=50, null=False)
    foto = models.ImageField(upload_to='media', null=False)
    sexo = models.CharField(max_length=6, blank=True, null=False, choices=(('macho', 'Macho'),
                                                                           ('hembra', 'Hembra')))
    
    raza = models.CharField(max_length=50, null=True)
    fecha = models.DateTimeField(auto_now=True, null=False)
    especie = models.CharField(max_length=5, blank=True, null=False, choices=(('perro', 'Perro'),
                                                                              ('gato', 'Gato')))
    edad = models.PositiveIntegerField(null=False)
    descripcion = models.CharField(max_length=500, null=False)
    usuario_futuro_duenio = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="+", null=True)

    estado = models.BooleanField(null=True)