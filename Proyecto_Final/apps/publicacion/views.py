from django.shortcuts import render, redirect
from django.forms import ModelForm
from apps.publicacion.models import Publicacion
from apps.publicacion.models import Contador
from apps.mascota.views import get_first_number_found
from apps.mascota.models import Mascota


class Post_Form(ModelForm):

    class Meta:
        model = Publicacion
        fields = {'descripcion', 'foto', 'especie', 'cantidad_de_mascotas'}
        labels = {'descripcion': 'Descripción General'}


def crear_publicacion(request):

    if request.method == 'POST':

        publicacion = Publicacion(usuario_creador=request.user,
                                  estado=True)

        form = Post_Form(request.POST, request.FILES, instance=publicacion)

        if form.is_valid():

            form.save()

            contador = Contador.objects.create(publicacion=publicacion, i=request.POST['cantidad_de_mascotas'])
            contador.save()

            return redirect(to='crear_mascota')

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


# __________________ELIMINAR PUBLICACION
# __________________LISTAR PUBLICACIONES
