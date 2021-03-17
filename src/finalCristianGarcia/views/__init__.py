from .home import HomeView
from .login import LoginView
from .dashboard import DashboardView
from .index import IndexView

#imports de reservas 
from .reserva import ReservaCreateView, ReservaListView, ReservaDeleteView, ReservaUpdateView, ReservaDetailView


#imports de huespedes
from .huesped import HuespedCreateView, HuespedListView, HuespedUpdateView, HuespedDeleteView, HuespedDetailView


#import de habitaciones
from .habitacion import HabitacionCreateView, HabitacionListView, HabitacionUpdateView, HabitacionDeleteView, HabitacionDetailView


#import del formulario 

from .formulario import NuevaReserva