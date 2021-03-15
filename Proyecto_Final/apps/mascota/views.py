from django.shortcuts import render, redirect
from django.forms import ModelForm
from apps.mascota.models import Mascota
from apps.publicacion.models import Publicacion
#from apps.publicacion.models import Contador
from apps.postulante.models import Postulante


class Pet_Form(ModelForm):

    class Meta:
        model = Mascota
        fields = ['foto', 'sexo', 'raza', 'edad', 'descripcion']
        labels = {'foto': 'Foto',
                  'sexo': 'Sexo',
                  'raza': 'Raza',
                  'edad': 'Edad',
                  'descripcion': 'Descripción'}


def crear_mascota(request):

    publicacion = Publicacion.objects.order_by('fecha').reverse().filter(usuario_creador=request.user)[0]

    '''pet_number = int(Contador.objects.order_by('id_contador').reverse()
                                 .filter(publicacion=publicacion)[0].i)'''

    if request.method == 'POST':

        mascota = Mascota(publicacion=publicacion,
                          estado=True)

        form = Pet_Form(request.POST, request.FILES, instance=mascota)

        if form.is_valid():

            form.save()

            # Se disminuye la variable contador en el campo i
            '''Contador.objects.order_by('id_contador').reverse().filter(publicacion=publicacion) \
                                                    .update(i=pet_number - 1)'''

            return redirect('ver_mis_publicaciones')
            
    else:
        form = Pet_Form()

    return render(request, 'publicacion/crear_mascota.html', {'form': form, 'pet_number': pet_number})


def ver_mascotas(request):

    mis_postulaciones = Postulante.objects.filter(usuario_postulado=request.user)
    context = {'mis_postulaciones': mis_postulaciones}

    if request.GET['publicacion']:

        publicacion = get_first_number_found(request.GET['publicacion'])
        mascotas = Mascota.objects.filter(publicacion=publicacion)

        lista = []

        for i in range(len(mascotas)):

            iguales = False

            for j in range(len(mis_postulaciones)):

                if mis_postulaciones[j].mascota.id_mascota == mascotas[i].id_mascota:

                    iguales = True
                    break

                else:
                    iguales = False

            if iguales:
                lista.append(True)
            else:
                lista.append(False)

        mascotas_dic = {}

        for i in range(len(mascotas)):

            mascotas_dic[mascotas[i]] = lista[i]

        context['mascotas_dic'] = mascotas_dic
        context['publicacion'] = publicacion

    return render(request, 'publicacion/ver_mascotas.html', context)


def get_first_number_found(text: str):

    i = 0

    for i in range(len(text)):

        if text[i].isdigit():
            break

    numbers = ''

    while i < len(text):

        if not text[i].isdigit():
            break

        numbers += text[i]
        i += 1

    return int(numbers)


# __________________ELIMINAR MASCOTA
# __________________EDICION DE DATOS DE MASCOTAS
# __________________LISTAR MASCOTAS
