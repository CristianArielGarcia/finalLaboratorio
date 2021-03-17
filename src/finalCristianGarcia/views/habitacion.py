from finalCristianGarcia.models import Habitacion
from finalCristianGarcia.forms import HabitacionForm, HabitacionUpdateForm, DateForm


from django.views.generic import TemplateView

#vistas genericas de django 
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


#para redireccionar despues de cierta accion
from django.urls import reverse_lazy

#mensajes 
from django.contrib.messages.views import SuccessMessageMixin


class HabitacionCreateView(CreateView):
    model= Habitacion 
    
    form_class = HabitacionForm
    
    template_name = "finalCristianGarcia/habitacion_create.html"
    
    success_message = 'Habitacion creado correctamente!'
    
    
    
class HabitacionListView(ListView):
    model = Habitacion
    
    template_name = "finalCristianGarcia/habitacion_list.html"
    
    queryset = Habitacion.objects.order_by('id')
    
    fields = 'numero_habitacion','hotel', 'cantidad_de_plazas'
    
    
    
class HabitacionUpdateView(UpdateView):
    model = Habitacion
    form_class = HabitacionUpdateForm
    template_name = 'finalCristianGarcia/habitacion_update.html'
    success_url = reverse_lazy('habitacion_list')
    


class HabitacionDeleteView(DeleteView):
    model = Habitacion
    template_name = 'finalCristianGarcia/habitacion_delete.html'
    success_url = reverse_lazy('habitacion_list')
    
    

class HabitacionDetailView(DetailView):
    
    model = Habitacion
    
    template_name = 'finalCristianGarcia/habitacion_detail.html'
    
    
    
