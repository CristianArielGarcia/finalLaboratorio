from finalCristianGarcia.models import Reserva, Huesped
from finalCristianGarcia.forms import ReservaHuespedForm


from django.urls import reverse_lazy


from django.views.generic.edit import FormView



class NuevaReserva(FormView):
    
    form_class = ReservaHuespedForm
    
    template_name = 'finalCristianGarcia/index2.html'
    
    success_url = reverse_lazy('home')

    def post(self, request, *args, **kwargs):
        form = ReservaHuespedForm(request.POST)
        if ((form.is_valid()) & (form.cleaned_data['fecha_de_ingreso'] < form.cleaned_data['fecha_de_egreso'])):
            
            #RECUPERO LOS DATOS DE LOS HUESPEDES
            
            nombre_huesped = form.cleaned_data['nombre']
            
            apellido_huesped = form.cleaned_data['apellido']
            
            tipo_documento_huesped = form.cleaned_data['tipo_documento']
            
            numero_documento_huesped = form.cleaned_data['numero_documento']
            
            mail_huesped = form.cleaned_data['mail']
            
            #creo el huesped
            huesped = Huesped(nombre_huesped, apellido_huesped, tipo_documento_huesped, numero_documento_huesped, mail_huesped)
            
            #guardo el huesped
            huesped.save()
            
            #RECUPERO LOS DATOS DE LA RESERVA 
            
            fecha_ingreso = form.cleaned_data['fecha_de_ingreso']
            
            fecha_egreso = form.cleaned_data['fecha_de_egreso']
            
            cantidad_huespedes = form.cleaned_data['cantidad_huespedes']
            
            
            
            #creo una reserva 
            reserva = Reserva(huesped = huesped, estado_reserva = False, fecha_de_ingreso = fecha_ingreso, fecha_de_egreso = fecha_egreso, cantidad_huespedes = cantidad_huespedes)
            
            #guardo la reserva
            reserva.save() 

            

        return super().post(request, *args, **kwargs)
