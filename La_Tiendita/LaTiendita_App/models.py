from django.db import models

# Create your models here.


class Productos(models.Model):
    codigo=models.CharField(max_length=4)
    nombre=models.CharField(max_length=30)
    tipo=models.CharField(max_length=30)
    marca=models.CharField(max_length=30)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    

class Clientes(models.Model):
    documento=models.CharField(max_length=10)
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    correo=models.EmailField(max_length=254)
    telefono=models.CharField(max_length=10)

