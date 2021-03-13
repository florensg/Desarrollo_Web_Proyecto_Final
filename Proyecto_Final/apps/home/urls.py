from django.urls import path
from apps.home import views


urlpatterns = [
    path('home/', views.index, name='home'),
]
