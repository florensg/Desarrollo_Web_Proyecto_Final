from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import send_mail



def enviar_correo (request):
    if request.method=="POST":
        subject=request.POST['asunto']

        message=request.POST['Mensaje']+ " | Remitente "+ request.POST['correo']
        
        email_from= settings.EMAIL_HOST_USER

        recipent_list=["FLOR Y AGUS!! AQUI SE PONE LA LISTA DE TODOS LOS CORREOS REGISTRADOS :)"]

        send_mail(subject, message, email_from, recipent_list)

        return redirect('gracias')
    return render(request, "contacto.html")

def gracias(request):
    return render(request, "gracias.html")    