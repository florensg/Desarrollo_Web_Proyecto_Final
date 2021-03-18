from django.shortcuts import render, redirect
from apps.postulante.models import Postulante
from apps.publicacion.models import Publicacion

def ver_postulantes(request,publicacion_id):
    context = {}

    publicacion = Publicacion.objects.get(id_publicacion=publicacion_id)
    postulante = Postulante.objects.filter(publicacion=publicacion,usuario_postulado=request.user)
    postulantes = Postulante.objects.filter(publicacion=publicacion_id)
    if request.method == 'GET':
        if not postulante.exists():
            postulacion = Postulante(publicacion=publicacion, usuario_postulado=request.user)
            postulacion.save()
        
            return redirect ('ver_postulantes',publicacion_id)
    context = {'postulantes' : postulantes,'publicacion' : publicacion}

    return render(request,'postulante/ver_postulantes.html',context)

