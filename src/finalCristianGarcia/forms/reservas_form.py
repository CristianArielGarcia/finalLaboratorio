from django import forms
from finalCristianGarcia.models import Reserva



class DateForm(forms.DateInput):
    input_type = 'date'
    
    
    



class ReservaForm(forms.ModelForm):

    class Meta:
        model = Reserva
        fields = "__all__"
        
        widgets= { 'fecha_de_ingreso': DateForm() , 'fecha_de_egreso': DateForm(), }

    def __init__(self, *args, **kwargs):
        super(ReservaForm, self).__init__(*args, **kwargs)
        
        #Datos datos reserva 
        
        reserva = self.instance
        
        #self.fields['fecha_de_ingreso']
        #self.fields['fecha_de_ingreso']
        
        #print(self.fields['fecha_de_ingreso'].initial 
        #self.fields['fecha_de_egreso'].queryset = Reserva.objects.filter(estado_reserva = False)
        

