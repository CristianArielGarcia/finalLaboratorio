from finalCristianGarcia.models import Huesped
from finalCristianGarcia.forms import HuespedForm, DateForm


from django.views.generic import TemplateView

#vistas genericas de django 
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


#para redireccionar despues de cierta accion
from django.urls import reverse_lazy

#mensajes 
from django.contrib.messages.views import SuccessMessageMixin


class HuespedCreateView(CreateView):
    model= Huesped 
    
    form_class = HuespedForm
    
    template_name = "finalCristianGarcia/huesped_create.html"
    
    success_message = 'Huesped creado correctamente!'


class HuespedListView(ListView):
    model = Huesped
    
    template_name = "finalCristianGarcia/huesped_list.html"
    
    queryset = Huesped.objects.order_by('numero_documento')
    
    fields = 'nombre','apellido', 'tipo_documento', 'numero_documento'
    
    
    
class HuespedUpdateView(UpdateView):
    model = Huesped
    form_class = HuespedForm
    template_name = 'finalCristianGarcia/huesped_update.html'
    success_url = reverse_lazy('huesped_list')
    


class HuespedDeleteView(DeleteView):
    model = Huesped
    template_name = 'finalCristianGarcia/huesped_delete.html'
    success_url = reverse_lazy('huesped_list')
    
    

class HuespedDetailView(DetailView):
    
    model = Huesped
    
    template_name = 'finalCristianGarcia/huesped_detail.html'
    
    
    
