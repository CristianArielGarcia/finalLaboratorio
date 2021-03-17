from django.db import models
from .reserva import Reserva
from .hotel import Hotel
from django.urls import reverse


class Habitacion(models.Model):
    cantidad_de_plazas = models.IntegerField()
    
    numero_habitacion = models.CharField(max_length= 5, null= False, blank=False, unique= True)
    
    descripcion = models.CharField(max_length=50, default='')
    
    precio_por_noche = models.FloatField()
    
    hotel = models.ForeignKey(Hotel, on_delete= models.CASCADE)
    
    reservas = models.ManyToManyField(Reserva, null= True, blank=True)
    
    def __str__(self):
        return 'Habitación: ' + self.numero_habitacion + ', hotel ' + self.hotel.nombre + ', ' + str(self.cantidad_de_plazas) + ' plazas.'
    
    
    def get_absolute_url(self):
        return reverse('habitacion_detail', kwargs={'pk':self.id})