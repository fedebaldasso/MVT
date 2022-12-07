from django.db import models
from datetime import datetime, date

# Create your models here.

class Familiar(models.Model):
    parentesco= models.CharField(max_length=50)
    nombre= models.CharField(max_length=50) 
    apellido=models.CharField(max_length=50) 
    edad=models.IntegerField()
    fecha_nacimiento=models.DateField(auto_now_add= False, auto_now= False, blank= True)
    
    