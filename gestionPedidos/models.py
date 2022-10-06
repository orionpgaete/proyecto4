from statistics import mode
from django.db import models

# Create your models here.

#Crear tablas Clientes, Articulos, Pedidos

class Clientes(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    email=models.EmailField()
    telefono=models.CharField(max_length=10)

class Articulos(models.Model):
    nombre = models.CharField(max_length=30)
    categoria = models.CharField(max_length=20)
    precio = models.IntegerField()

class Pedidos(models.Model):
    nrodcto = models.IntegerField()
    fecha_emision = models.DateField()
    entregado = models.BooleanField()

    #python manage.py shell   -> abre consola
    