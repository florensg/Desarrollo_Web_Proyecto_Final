from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import send_mail
from apps.mensaje.models import Chat


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

    context = {'chats': Chat.objects.filter(usuario_creador=request.user)}

    return render(request, "mensaje/lista_de_chats.html", context)


def chat(request, id_chat: int):

    context = {}

    print(id_chat)

    return render(request, "mensaje/lista_de_chats.html", context)
