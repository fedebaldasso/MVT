from django.shortcuts import render
from .models import Familiar
from django.http import HttpResponse

# Create your views here.

def familiar(request):
    pariente= Familiar(parentesco="Padre", nombre="Roberto", apellido="Baldasso", edad=55)
    pariente.save()
    cadena_texto=f"Familiar Guardado: Nombre {pariente.parentesco}, Nombre: {pariente.nombre}"
    return HttpResponse(cadena_texto)
