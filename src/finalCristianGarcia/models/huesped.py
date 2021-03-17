from django.db import models
from django.urls import reverse


class Huesped(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=70)
    
    DNI = 'DNI'
    PS = 'PS'
    tipos_de_documentos = (
        (DNI, 'Dni'),
        (PS, 'Pasaporte'),
    )
    
    tipo_documento = models.CharField(
        max_length= 3,
        choices= tipos_de_documentos,
        default=DNI,
    )
    
    numero_documento = models.CharField(primary_key=True, max_length= 10)
    
    mail = models.EmailField()
    
    def __str__(self):
        return self.nombre + " " + self.apellido + " " + self.tipo_documento + ": " + str(self.numero_documento)
    
    
    
    def get_absolute_url(self):
        return reverse('huesped_detail', kwargs={'pk':self.numero_documento})
        #return reverse('home')