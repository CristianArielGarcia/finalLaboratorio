from django.db import models


class Hotel(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    foto = models.ImageField() 
    reseña = models.TextField(default="")
    
    
    def __str__(self):
        return self.nombre
    