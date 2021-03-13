from django.urls import path
from apps.registrate import views


urlpatterns = [
    path('registrate/', views.registro, name='registrate'),
]
