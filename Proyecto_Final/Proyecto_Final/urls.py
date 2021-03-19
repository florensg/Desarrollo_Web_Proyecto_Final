"""Proyecto_Final URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include,re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import reverse_lazy

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include('apps.home.urls')),
    path('', include('apps.registrate.urls')),
    path('', include('django.contrib.auth.urls')),
    path('', include('apps.publicacion.urls')),
    path('', include('apps.usuario.urls')),
    path('', include('apps.denuncia.urls')),
    path('', include('apps.postulante.urls')),
    path('', include('apps.mensaje.urls')),
    path('reset/password_reset', PasswordResetView.as_view(template_name='registration/password_reset_form.html',
        email_template_name='registration/password_reset_email.html'), 
        name='password_reset'),
    path('reset/password_reset_done',PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), 
        name='password_reset_done'),
    re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), 
        name='password_reset_confirm'),
    path('reset/done', PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), 
        name='password_reset_complete')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
