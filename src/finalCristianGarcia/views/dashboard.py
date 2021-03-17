from django.views.generic import ListView
from finalCristianGarcia.models import Reserva
from django.contrib.auth.mixins import LoginRequiredMixin

class DashboardView(LoginRequiredMixin, ListView):
    model = Reserva
    template_name = 'finalCristianGarcia/dashboard.html'
    
    
    def get_queryset(self):
        #mando a la vista todas las reservas que están asignadas ya 
        queryset = self.model.objects.filter(estado_reserva = True)
        
        return queryset