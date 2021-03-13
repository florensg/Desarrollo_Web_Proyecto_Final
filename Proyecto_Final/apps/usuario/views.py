from django.shortcuts import redirect, render
from apps.publicacion.models import Publicacion
from apps.mascota.models import Mascota
from .models import Usuario
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.forms import UserCreationForm


def ver_perfil(request):

    context = {'n_calificaciones': 0,
               'publicaciones_usuario': Publicacion.objects.filter(usuario_creador=request.user),
               'mascotas': Mascota.objects.all}

    return render(request, "usuario/ver_perfil.html", context)

def ver_usuario_externo(request):
	context = {}

	if request.GET.get('usuario_creador'):

		publicacion = Publicacion.objects.filter(usuario_creador=request.GET.get('publicacion.usuario_creador'))
		context = {'publicacion' : publicacion, 'usuario' : request.GET.get('publicacion.usuario_creador')}
	return render(request, "usuario/ver_usuario_externo.html",context)


class UserForm(UserChangeForm):

    class Meta:
        model = Usuario
        fields = ['first_name', 'last_name', 'sexo', 'provincia', 'ciudad', 'email', 'descripcion_propia']

    def __init__(self, *args, **kwargs):
    	super(self.__class__, self).__init__(*args, **kwargs)
    	self.fields['first_name'].required=False
    	self.fields['last_name'].required=False
    	self.fields['sexo'].required=False
    	self.fields['provincia'].required=False
    	self.fields['ciudad'].required=False
    	self.fields['email'].required=False
    	self.fields['descripcion_propia'].required=False
    	


def editar_perfil(request):
	form = UserForm(request.POST,request.FILES)

	if request.POST:
		if form['first_name'].value():
			Usuario.objects.filter(username=request.user.username).update(first_name=form['first_name'].value())
		if form['last_name'].value():
			Usuario.objects.filter(username=request.user.username).update(last_name=form['last_name'].value())
		if form['sexo'].value():
			Usuario.objects.filter(username=request.user.username).update(sexo=form['sexo'].value())
		if form['provincia'].value():
			Usuario.objects.filter(username=request.user.username).update(provincia=form['provincia'].value())
		if form['ciudad'].value():
			Usuario.objects.filter(username=request.user.username).update(ciudad=form['ciudad'].value())
		if form['email'].value():
			Usuario.objects.filter(username=request.user.username).update(email=form['email'].value())
		if form['descripcion_propia'].value():
			Usuario.objects.filter(username=request.user.username).update(descripcion_propia=form['descripcion_propia'].value())
		return redirect('ver_perfil')

	return render(request, "usuario/editar_perfil.html", {'form':form})

