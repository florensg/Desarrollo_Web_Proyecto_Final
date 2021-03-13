from django.http import HttpResponse
from django.template import loader
import datetime


def saludo(request):

    now = datetime.datetime.now()
    template = loader.get_template("index.html")
    context = {"hora": now,
               "alumno": "felipe"}

    return HttpResponse(template.render(context, request))
