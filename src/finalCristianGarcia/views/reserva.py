from finalCristianGarcia.models import Reserva
from finalCristianGarcia.forms import ReservaForm, DateForm
from django.core.mail import send_mail
from django.conf import settings


from django.views.generic import TemplateView

#vistas genericas de django 
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


#para redireccionar despues de cierta accion
from django.urls import reverse_lazy

#mensajes 
from django.contrib.messages.views import SuccessMessageMixin


class ReservaCreateView(CreateView):
    model= Reserva 
    
    form_class = ReservaForm
    
    template_name = "finalCristianGarcia/reserva_create.html"
    
    success_message = 'Reserva creada correctamente!'


class ReservaListView(ListView):
    model = Reserva
    
    template_name = "finalCristianGarcia/reservas_list.html"
    
    queryset = Reserva.objects.order_by('numero_reserva')
    
    fields = 'numero_reserva','fecha_de_ingreso', 'fecha_de_egreso', 'huesped.dni'
    
    
    
class ReservaUpdateView(UpdateView):
    model = Reserva
    form_class = ReservaForm
    template_name = 'finalCristianGarcia/reserva_update.html'
    success_url = reverse_lazy('reserva_list')
    
    
    #si no anda sacar de aca para abajo / hay que sacarlo porque no puede enviar mail porque no se conecta a internet 
    '''
    def post(self, request, *args, **kwargs):
        
        form = ReservaForm(request.POST)
        
        if form.is_valid():
            
            mail_huesped = form.cleaned_data['huesped'].mail
            
            estadoreserva = form.cleaned_data['estado_reserva']
            
            fecha_ingreso = str(form.cleaned_data['fecha_de_ingreso'])
            
            fecha_egreso = str(form.cleaned_data['fecha_de_egreso'])
            
            cant_huespedes = str(form.cleaned_data['cantidad_huespedes'])
            
            subject = "Estado de la reserva"
            
            content = 'Su reserva queda confirmada. Ingreso: ' + fecha_ingreso + ' salida: ' + fecha_egreso + ' para ' + cant_huespedes + ' personas.'
            
            content2 = "Lamentablemente no tenemos disponibilidad dentro del periodo de tiempo seleccionado."
            
            
            if request.method == 'POST' and estadoreserva and mail_huesped:
                send_mail(subject, content, settings.EMAIL_HOST_USER, [mail_huesped], fail_silently=False)
            else:
                send_mail(subject, content2, settings.EMAIL_HOST_USER, [mail_huesped], fail_silently=False)
        '''


class ReservaDeleteView(DeleteView):
    model = Reserva
    template_name = 'finalCristianGarcia/reserva_delete.html'
    success_url = reverse_lazy('reserva_list')
    
    

class ReservaDetailView(DetailView):
    
    model = Reserva
    
    template_name = 'finalCristianGarcia/reserva_detail.html'
    
    
