from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from apps.usuario.models import Usuario


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = Usuario
        fields = ['first_name', 'last_name', 'sexo', 'provincia', 'ciudad',
                  'username', 'email', 'password1', 'password2']
        labels = {'sexo': 'Sexo',
                  'provincia': 'Provincia',
                  'ciudad': 'Ciudad'}


def registro(request):

    context = {'formulario': CustomUserCreationForm}

    if request.method == 'POST':

        formulario = CustomUserCreationForm(data=request.POST)

        if formulario.is_valid():

            formulario.save()

            user = authenticate(username=formulario.cleaned_data['username'],
                                password=formulario.cleaned_data['password1'])
            login(request, user)

            return redirect(to='home')

        context['formulario'] = formulario

    return render(request, 'registration/registrate.html', context)
