from django.shortcuts import render, redirect
from apps.postulante.models import Postulante
from apps.publicacion.models import Publicacion

def ver_postulantes(request,publicacion_id):

    postulante = Postulante.objects.filter(publicacion=publicacion_id)
    context = {'postulantes' : postulante}
    return render(request,'publicacion/ver_postulantes.html',context)

def postularse(request):

    context = {}
    publicacion = Publicacion.objects.get(id_publicacion=publicacion_id)
    if request.method == 'GET':

        postulante = Postulante(publicacion=publicacion, usuario_postulado=request.user)
        postulante.save()

        return redirect(to='ver_publicaciones')
    context['publicacion'] = publicacion
    return render(request,'publicacion/ver_postulantes.html',context)
