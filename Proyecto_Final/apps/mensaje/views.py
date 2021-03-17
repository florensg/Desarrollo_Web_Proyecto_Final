from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import send_mail
from apps.mensaje.models import Chat
from apps.mensaje.models import Mensaje


def enviar_correo (request):

    if request.method == "POST":

        subject = request.POST['asunto']

        message = request.POST['Mensaje'] + " | Remitente " + request.POST['correo']
        
        email_from = settings.EMAIL_HOST_USER

        recipent_list = ["FLOR Y AGUS!! AQUI SE PONE LA LISTA DE TODOS LOS CORREOS REGISTRADOS :)"]

        send_mail(subject, message, email_from, recipent_list)

        return redirect('gracias')

    return render(request, "contacto.html")


def gracias(request):

    return render(request, "gracias.html")


def lista_de_chats(request):

    c_del_creador = Chat.objects.filter(usuario_creador=request.user)
    c_del_futuro_duenio = Chat.objects.filter(usuario_futuro_duenio=request.user)

    context = {'chats': c_del_creador.union(c_del_futuro_duenio).order_by('-id_chat')}

    return render(request, 'mensaje/lista_de_chats.html', context)


def chat(request, id_chat: int):

    context = {'mensajes': Mensaje.objects.filter(chat=id_chat),
               'id_chat': id_chat}

    return render(request, 'mensaje/chat.html', context)


def enviar_mensaje(request, id_chat: int):

    context = {}

    if request.GET['mensaje']:

        i_chat = Chat.objects.filter(id_chat=id_chat)[0]

        mensaje = Mensaje(chat=i_chat, usuario_emisor=request.user, mensaje=request.GET['mensaje'])
        mensaje.save()

        return redirect(to='http://127.0.0.1:8000/chat/' + id_chat.__str__())

    return render(request, 'mensaje/enviar_mensaje.html', context)
