from django.shortcuts import redirect, render
from apps.publicacion.models import Publicacion
from .models import Usuario, Calificacion
from django.contrib.auth.forms import UserChangeForm
from django.utils.datastructures import MultiValueDictKeyError


def ver_perfil(request):

	context = {'calificaciones': Calificacion.objects.filter(usuario_calificado=request.user)}

	return render(request, "usuario/ver_perfil.html", context)


def ver_usuario_externo(request, usuario_id):

	context = {}

	usuario = Usuario.objects.get(id=usuario_id)
	publicacion = Publicacion.objects.filter(usuario_creador=usuario_id)
	calificaciones = Calificacion.objects.filter(usuario_calificado=usuario)

	if request.method == 'GET':
		context = {'usuario': usuario, 'publicacion': publicacion, 'calificaciones': calificaciones}

	return render(request, 'usuario/ver_usuario_externo.html', context)


class UserForm(UserChangeForm):

	class Meta:
		model = Usuario
		fields = ['first_name', 'last_name', 'sexo', 'provincia', 'ciudad', 'email', 'descripcion_propia']

	def __init__(self, *args, **kwargs):

		super(self.__class__, self).__init__(*args, **kwargs)
		self.fields['first_name'].required = False
		self.fields['last_name'].required = False
		self.fields['sexo'].required = False
		self.fields['provincia'].required = False
		self.fields['ciudad'].required = False
		self.fields['email'].required = False
		self.fields['descripcion_propia'].required = False


def editar_perfil(request, usuario_id):

	instancia = Usuario.objects.get(id=usuario_id)

	form = UserForm(instance=instancia)

	if request.method == 'POST':
		form = UserForm(request.POST, instance=instancia)

	if form.is_valid():

		instancia = form.save(commit=False)
		instancia.save()

		return redirect('ver_perfil')

	return render(request, "usuario/editar_perfil.html", {'form': form})


def calificar_usuario(request):

	publicacion = Publicacion.objects.get(id_publicacion=request.GET['id_publicacion'])
	context = {'publicacion': publicacion}

	try:
		if request.GET['calificacion']:

			calificacion = Calificacion(usuario_calificador=request.user,
										usuario_calificado=publicacion.usuario_futuro_duenio,
										calificacion=request.GET['calificacion'],
										comentario=request.GET['comentario'])
			calificacion.save()

			usuario = Usuario.objects.get(id=publicacion.usuario_futuro_duenio.id)

			# Se actualiza la cantidad de calificaciones
			usuario.cantidad_de_calificaciones = usuario.cantidad_de_calificaciones + 1

			calificaciones = Calificacion.objects.filter(usuario_calificado=publicacion.usuario_futuro_duenio)
			usuario.save()

			sumatoria = 0

			for calificacion_i in calificaciones:
				sumatoria = sumatoria + calificacion_i.calificacion

			usuario = Usuario.objects.get(id=publicacion.usuario_futuro_duenio.id)

			# Se actualiza el promedio de calificaciones
			usuario.promedio_calificacion = sumatoria / usuario.cantidad_de_calificaciones
			usuario.save()

			return redirect('ver_usuario_externo', publicacion.usuario_futuro_duenio.id)

	except MultiValueDictKeyError:
		pass

	return render(request, "usuario/calificar_usuario.html", context)
