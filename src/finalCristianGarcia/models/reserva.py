from django.db import models
from .huesped import Huesped
from django.urls import reverse


class Reserva(models.Model): 
    
    huesped = models.ForeignKey(Huesped, on_delete = models.CASCADE)
    
    
    PENDIENTE = False
    ASIGNADA = True
    estado = (
        (PENDIENTE, 'Pendiente de asignacion'),
        (ASIGNADA, 'Asignada'),
    )
    
    estado_reserva = models.BooleanField(
        max_length= 9,
        choices= estado,
        default= PENDIENTE,
    )
    
    numero_reserva = models.AutoField(primary_key= True)
    
    fecha_de_ingreso = models.DateField(auto_now_add= False)
    fecha_de_egreso = models.DateField(auto_now_add= False)
    
    cantidad_huespedes = models.IntegerField()
    
    
    
    def __str__(self):
        return  'Nro. de reserva: ' + str(self.numero_reserva) + ". Ingreso: " + self.fecha_de_ingreso.strftime('%d-%m-%Y') + ". Egreso: " + self.fecha_de_egreso.strftime('%d-%m-%Y') + '. Plazas: ' + str(self.cantidad_huespedes)
    
    
    
    def get_absolute_url(self):
        return reverse('reserva_detail', kwargs={'pk':self.numero_reserva})
        #return reverse('home')