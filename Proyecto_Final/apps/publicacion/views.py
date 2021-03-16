from django.shortcuts import render, redirect
from django.forms import ModelForm
from apps.publicacion.models import Publicacion
from apps.mascota.views import get_first_number_found
from apps.mascota.models import Mascota


class Post_Form(ModelForm):

    class Meta:
        model = Publicacion
        fields = {'nombre', 'descripcion', 'foto', 'especie', 'sexo', 'raza', 'edad'}
        labels = {'descripcion': 'Descripción General'}

def crear_publicacion(request):

    if request.method == 'POST':

        publicacion = Publicacion(usuario_creador=request.user,
                                  estado=True)

        form = Post_Form(request.POST, request.FILES, instance=publicacion)

        if form.is_valid():

            form.save()

            return redirect(to='ver_mis_publicaciones')

    else:
        form = Post_Form()

    return render(request, 'publicacion/crear_publicacion.html', {'form': form})


def ver_mis_publicaciones(request):

    context = {'publicaciones': Publicacion.objects.filter(usuario_creador=request.user)}

    return render(request, "publicacion/ver_mis_publicaciones.html", context)


def confirmar_eliminacion(request):

    context = {}

    if request.GET['publicacion']:

        publicacion_a_eliminar = get_first_number_found(request.GET['publicacion'])
        publicacion = Publicacion.objects.filter(id_publicacion=publicacion_a_eliminar)[0]

        context = {'publicacion': publicacion,
                   'publicacion_a_eliminar': publicacion_a_eliminar}

    return render(request, 'publicacion/eliminar_publicacion.html', context)


def eliminar_publicacion(request):

    if request.GET['publicacion_a_eliminar']:

        publicacion = request.GET['publicacion_a_eliminar']

        Publicacion.objects.filter(id_publicacion=publicacion).delete()
        Mascota.objects.filter(publicacion=publicacion).delete()

    return redirect(to='ver_mis_publicaciones')

#publicaciones sin filtrar
def ver_publicaciones_A(request):

    context = {'publicaciones': Publicacion.objects.all}

    return render(request, 'publicacion/ver_publicaciones_A.html', context)

#publicaciones filtradas
def ver_publicaciones_B(request):

    context = {}

    if request.GET['especie']:

        especie = request.GET['especie']

        publicaciones = Publicacion.objects.filter(especie=especie)

        if especie == 'perro':
            especie = 'Perro'
        else:
            especie = 'Gato'

        context = {'publicaciones': publicaciones,
                   'especie': especie}

    return render(request, 'publicacion/ver_publicaciones_B.html', context)

class PublicacionForm(ModelForm):

    class Meta:
        model = Publicacion
        fields = ['nombre', 'foto', 'sexo', 'raza', 'especie', 'edad', 'descripcion']

    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        self.fields['nombre'].required=False
        self.fields['foto'].required=False
        self.fields['sexo'].required=False
        self.fields['raza'].required=False
        self.fields['especie'].required=False
        self.fields['edad'].required=False
        self.fields['descripcion'].required=False


def editar_publicacion(request,publicacion_id):

    instancia = Publicacion.objects.get(id_publicacion=publicacion_id)
    
    form = PublicacionForm(instance=instancia)

    if request.method == 'POST':

        form = PublicacionForm(request.POST,request.FILES, instance= instancia)

    if form.is_valid():

        instancia = form.save(commit=False)
        instancia.save()

        return redirect('ver_mis_publicaciones')

    return render(request, 'publicacion/editar_publicacion.html', {'form':form})

def ver_publicacion_usuario_externo(request,usuario_id):

    if request.method == 'GET':
        publicaciones = Publicacion.objects.filter(usuario_creador=usuario_id)
    context = {'publicaciones': publicaciones}

    return render(request, "publicacion/ver_publicacion_usuario_externo.html", context)


# __________________ELIMINAR PUBLICACION
# __________________LISTAR PUBLICACIONES
