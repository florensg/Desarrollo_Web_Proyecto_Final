from django.urls import path
from apps.postulante import views


urlpatterns = [
    path('postularse/<int:publicacion_id>', views.postularse, name='postularse'),
]
