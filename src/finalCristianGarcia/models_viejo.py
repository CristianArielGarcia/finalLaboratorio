from django.db import models


class Hotel(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    foto = models.ImageField() 
    reseña = models.TextField(default="")
    
    
    def __str__(self):
        return self.nombre
    
    
    
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
    
    mail = models.CharField(max_length= 60)
    
    numero_documento = models.CharField(primary_key=True, max_length= 10)
    
    
    def __str__(self):
        return self.nombre + " " + self.apellido + " " + self.tipo_documento + ": " + str(self.numero_documento)
    
    
    
    
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
    '''
    esto es un integer porque cuando quiera asignar una reserva a multiples habitaciones, voy a sumar la cantidad de plazas que soportan las habitaciones seleccionadas
    para evitar asignar habitaciones con menos plazas a la reserva.
    '''
    
    
    
    
    def __str__(self):
        return  'Numero de reserva: ' + str(self.numero_reserva) + " Ingreso: " + self.fecha_de_ingreso.strftime('%d-%m-%Y') + ". Egreso: " + self.fecha_de_egreso.strftime('%d-%m-%Y')



class Habitacion(models.Model):
    cantidad_de_plazas = models.IntegerField()
    '''
    esto es un integer porque cuando quiera asignar una reserva a multiples habitaciones, voy a sumar la cantidad de plazas que soportan las habitaciones seleccionadas
    para evitar asignar habitaciones con menos plazas a la reserva.
    '''
    
    numero_habitacion = models.CharField(max_length= 5, null= False, blank=False, unique= True)
    
    descripcion = models.CharField(max_length=50, default='')
    
    precio_por_noche = models.FloatField()
    
    hotel = models.ForeignKey(Hotel, on_delete= models.CASCADE)
    
    
    reservas = models.ForeignKey(Reserva, on_delete= models.CASCADE, null= True, blank=True)
    
    def __str__(self):
        return 'Habitación: ' + self.numero_habitacion + ', hotel ' + self.hotel.nombre + ', ' + str(self.cantidad_de_plazas) + ' plazas.'
