from django.db import models
from apps.usuario.models import Usuario
from django.contrib import admin

class Denuncia(models.Model):
    id_denuncia = models.AutoField(primary_key=True)

    usuario_denunciante = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="+", null=True)
    usuario_denunciado = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="+", null=True)
    fecha = models.DateTimeField(auto_now=True, null=False)
    tipo = models.CharField(max_length=1, blank=True, null=False,
                            choices=(('a', 'Dato/s falso/s en publicaciones'),
                                     ('b', 'Los animales no tienen todas las vacunas necesarias'),
                                     ('c', 'Sobreexplotación al animal hembra'),
                                     ('d', 'Maltrato animal')))
    comentario = models.CharField(max_length=1500, null=False)
    estado = models.BooleanField(null=True)

class DenunciaAdmin(admin.ModelAdmin):
    list_display = ('usuario_denunciante','usuario_denunciado','fecha','tipo')
    list_filter = ('tipo','estado')