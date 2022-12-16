from django.shortcuts import render
from .models import Familiar
from django.http import HttpResponse
import datetime
from django.template import Template, Context, loader

# Create your views here.

def inicio(request):
    return HttpResponse("Estoy en el inicio!")

def familiar(request):
    familiar1= Familiar(parentesco="Padre", nombre="Roberto", apellido="Baldasso", edad=67, fecha_nacimiento="1955-07-17")
    familiar1.save()
    familiar2= Familiar(parentesco="Madre", nombre="Liliana", apellido="Martínez", edad=63, fecha_nacimiento="1959-09-30")
    familiar2.save()
    familiar3= Familiar(parentesco="Hermano", nombre="Franco", apellido="Baldasso", edad=27, fecha_nacimiento="1995-07-02")
    familiar3.save()
    familiares= {familiar1,familiar2,familiar3}
    
    # template= loader.get_template("template1.html") #Abre, lee y cierra el archivo

    # familia=template.render(familiares)#Llena mis espacios en blanco con los datos de mi contexto
    return render(request,"template1.html", {"parientes":familiares})
    # return HttpResponse(familia)







    