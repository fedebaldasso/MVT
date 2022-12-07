from django.shortcuts import render
from .models import Familiar
from django.http import HttpResponse
import datetime
from django.template import Template, Context, loader

# Create your views here.

def inicio(request):
    return HttpResponse("Estoy en el inicio!")

def familiar(request):
    pariente= Familiar(parentesco="Padre", nombre="Roberto", apellido="Baldasso", edad=67, fecha_nacimiento="1955-07-17")
    pariente.save()
    parientes= {"parentesco": pariente.parentesco, "nombre": pariente.nombre, "apellido": pariente.apellido, "edad": pariente.edad, "fecha_nacimiento": pariente.fecha_nacimiento }
    
    template= loader.get_template("template1.html") #Abre, lee y cierra el archivo

    familiares=template.render(parientes)#Llena mis espacios en blanco con los datos de mi contexto
    return HttpResponse(familiares)







    