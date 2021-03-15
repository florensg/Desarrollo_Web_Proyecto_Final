from django.shortcuts import render, redirect
from apps.postulante.models import Postulante
from apps.publicacion.models import Publicacion


def confirmar_postulacion1(request):

    context = {}

    '''if request.GET['mascota']:
            
                    mascota = get_first_number_found(request.GET['mascota'])
                    postulantes = Postulante.objects.filter(mascota=mascota)
            
                    context = {'postulantes': postulantes,
                               'mascota': mascota}'''

    return render(request, 'publicacion/postularse.html', context)


def postularse(request,publicacion_id):

    context = {}
    publicacion = Publicacion.objects.get(id_publicacion=publicacion_id)
    if request.method == 'GET':

        postulante = Postulante(publicacion=publicacion, usuario_postulado=request.user)
        postulante.save()

        return redirect('ver_publicaciones_A')

    return render(request,'publicacion/postularse.html',context)
