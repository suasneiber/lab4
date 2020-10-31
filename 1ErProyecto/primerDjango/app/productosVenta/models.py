from django.db import models

# Create your models here.

class productoVenta(models.Model):
    id = models.CharField(max_length=3, primary_key=True)
    nombre = models.CharField(max_length=30)
    cantidad = models.CharField(max_length=3)
    precio = models.CharField(max_length=4)
    codigo = models.CharField(max_length=13)
    tipo = models.CharField(max_length=10)
