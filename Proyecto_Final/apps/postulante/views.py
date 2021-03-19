from django.shortcuts import render, redirect
from apps.postulante.models import Postulante
from apps.publicacion.models import Publicacion
from apps.usuario.models import Usuario
from apps.mensaje.models import Chat
from django.utils.datastructures import MultiValueDictKeyError


def ver_postulantes(request, id_publicacion):

    postulantes = Postulante.objects.filter(publicacion=id_publicacion)
    publicacion = Publicacion.objects.get(id_publicacion=id_publicacion)

    context = {'postulantes': postulantes, 'publicacion': publicacion}

    try:
        if request.GET['postularse']:

            postulante = Postulante.objects.filter(publicacion=publicacion, usuario_postulado=request.user)

            if not postulante.exists():

                postulacion = Postulante(publicacion=publicacion, usuario_postulado=request.user)
                postulacion.save()

                return redirect('ver_postulantes', id_publicacion)

    except MultiValueDictKeyError:
        pass

    return render(request, 'postulante/ver_postulantes.html', context)


def elegir_duenio(request, id_publicacion: int):

    publicacion = Publicacion.objects.get(id_publicacion=id_publicacion)

    context = {'postulantes': Postulante.objects.filter(publicacion=publicacion),
               'publicacion': publicacion}

    return render(request, 'postulante/elegir_duenio.html', context)


def hacer_duenio(request):

    id_publicacion = request.GET['id_publicacion']

    if request.GET['usuario_elegido']:

        usuario_elegido = Usuario.objects.get(id=Usuario.objects.get(username=request.GET['usuario_elegido']).id)

        publicacion = Publicacion.objects.get(id_publicacion=id_publicacion)

        publicacion.usuario_futuro_duenio = usuario_elegido
        publicacion.estado = False

        publicacion.save()

        nuevo_chat = Chat(publicacion=publicacion,
                          usuario_creador=publicacion.usuario_creador,
                          usuario_futuro_duenio=publicacion.usuario_futuro_duenio,
                          estado=True)
        nuevo_chat.save()

    return redirect('ver_postulantes', id_publicacion)
