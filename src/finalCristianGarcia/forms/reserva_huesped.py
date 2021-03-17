from django import forms
from finalCristianGarcia.models import Reserva, Huesped
from bootstrap_datepicker_plus import DatePickerInput



class DateInput(forms.DateInput):
    input_type = 'date'



class ReservaHuespedForm (forms.Form):


    #CAMPOS DEL HUESPED
    
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=70)
    
    
    DNI = 'DNI'
    PS = 'PS'
    tipos_de_documentos = (
        (DNI, 'Dni'),
        (PS, 'Pasaporte'),
    )
    
    tipo_documento = forms.ChoiceField(
        choices= tipos_de_documentos,
    )
    
    numero_documento = forms.CharField( max_length= 10)
    
    mail = forms.EmailField()
    
    
    #CAMPOS DE LA RESERVA
    
    PENDIENTE = False
    ASIGNADA = True
    estado = (
        (PENDIENTE, 'Pendiente de asignacion'),
        (ASIGNADA, 'Asignada'),
    )
    
    
    fecha_de_ingreso = forms.DateField( widget=DateInput )
    
    
    fecha_de_egreso = forms.DateField( widget=DateInput )

    cantidad_huespedes = forms.IntegerField()
    
    
    