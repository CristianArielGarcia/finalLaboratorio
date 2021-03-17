from django import forms         
from finalCristianGarcia.models import Habitacion, Reserva



class HabitacionForm(forms.ModelForm):
    
    class Meta:
        model = Habitacion
        fields = "__all__"
        
    def __init__(self, *args, **kwargs):
        super(HabitacionForm, self).__init__(*args, **kwargs)
        
        #Datos habitacion
        
        self.fields['reservas'].queryset = Reserva.objects.filter(estado_reserva = False)
        


class HabitacionUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Habitacion
        fields = "__all__"