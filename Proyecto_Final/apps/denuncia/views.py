from django.shortcuts import render, redirect
from django.forms import ModelForm
from apps.denuncia.models import Denuncia
from apps.usuario.models import Usuario

class Post_Form(ModelForm):

    class Meta:
        model = Denuncia

        fields = {'tipo', 'comentario'}
        labels = {  'tipo': 'Tipo',
                    'comentario': 'Comentario'}


def crear_denuncia(request,usuario_id):
    context = {}
    usuario = Usuario.objects.get(id=usuario_id)
    if request.method == 'POST':

        denuncia = Denuncia(usuario_denunciado=usuario, usuario_denunciante=request.user, estado=True)

        form = Post_Form(request.POST, request.FILES, instance=denuncia)

        if form.is_valid():

            form.save()

            return redirect('ver_usuario_externo', usuario_id)

    else:
        form = Post_Form()

    context = {'usuario' : usuario, 'form' : form}
    return render(request, 'denuncia/crear_denuncia.html', context)
