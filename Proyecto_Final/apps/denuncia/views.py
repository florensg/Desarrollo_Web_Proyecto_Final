from django.shortcuts import render, redirect
from django.forms import ModelForm
from apps.denuncia.models import Denuncia

class Post_Form(ModelForm):

    class Meta:
        model = Denuncia

        fields = {'usuario_denunciante', 'usuario_denunciado', 'tipo', 'comentario'}
        labels = {  'usuario_denunciante': 'Usuario denunciante',
                    'usuario_denunciado': 'Usuario denunciado',
                    'tipo': 'Tipo',
                    'comentario': 'Comentario'}


def crear_denuncia(request):

    if request.method == 'POST':

        denuncia = Denuncia(usuario_denunciado=request.user,
                                  estado=True)

        form = Post_Form(request.POST, request.FILES, instance=denuncia)

        if form.is_valid():

            form.save()

            return redirect(to='ver_usuario_externo')

    else:
        form = Post_Form()

    return render(request, 'denuncia/crear_denuncia.html', {'form': form})
