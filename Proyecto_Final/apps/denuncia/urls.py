from django.urls import path
from apps.denuncia import views


urlpatterns = [
    path('crear_denuncia/', views.crear_denuncia, name='crear_denuncia'),
    
]