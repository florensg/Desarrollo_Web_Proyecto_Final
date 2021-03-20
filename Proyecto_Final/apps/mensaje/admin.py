from django.contrib import admin
from .models import *

admin.site.register(Mensaje,MensajeAdmin)
admin.site.register(Chat,ChatAdmin)