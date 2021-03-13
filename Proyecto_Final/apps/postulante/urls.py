from django.urls import path
from apps.postulante import views


urlpatterns = [
    path('confirmar_postulacion/', views.confirmar_postulacion, name='confirmar_postulacion'),
    path('postularce/', views.postularce, name='postularce'),
]
