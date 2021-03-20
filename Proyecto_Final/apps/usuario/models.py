from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib import admin

class Usuario(AbstractUser):

    sexo = models.CharField(max_length=30, blank=True, null=False, choices=(('masculino', 'Masculino'),
                                                                            ('femenino', 'Femenino'),
                                                                            ('otro', 'Otro')))
    provincia = models.CharField(max_length=50, null=True)
    ciudad = models.CharField(max_length=50, null=False)
    descripcion_propia = models.CharField(max_length=2000, null=True)
    cantidad_de_calificaciones = models.IntegerField(null=True)
    promedio_calificacion = models.FloatField(null=True)

    
class UsuarioAdmin(admin.ModelAdmin):
	list_display = ('id','username','first_name','last_name','sexo','provincia','ciudad','promedio_calificacion')
	list_filter = ('sexo','provincia','ciudad')

    
class Calificacion(models.Model):
    id_calificacion = models.AutoField(primary_key=True)

    usuario_calificador = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="+", null=False)
    usuario_calificado = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="+", null=False)
    calificacion = models.IntegerField(null=False)
    comentario = models.CharField(max_length=2000, null=False)
