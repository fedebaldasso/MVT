from django.db import models

# Create your models here.

class Familiar(models.Model):
    parentesco= models.CharField(max_length=50)
    nombre= models.CharField(max_length=50) 
    apellido=models.CharField(max_length=50) 
    edad=models.IntegerField()
    
    