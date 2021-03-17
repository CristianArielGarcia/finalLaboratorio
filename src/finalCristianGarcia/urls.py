from django.urls import path, include
from finalCristianGarcia.views import ( 
    HomeView,
    LoginView, DashboardView, IndexView, NuevaReserva,
    
    #Reservas
    ReservaCreateView, ReservaListView, ReservaDeleteView, ReservaUpdateView, ReservaDetailView,
    
    
    #Huesped
    HuespedCreateView, HuespedListView, HuespedUpdateView, HuespedDeleteView, HuespedDetailView,
    
    
    #Habitacion 
    
    HabitacionCreateView, HabitacionListView, HabitacionUpdateView, HabitacionDeleteView, HabitacionDetailView,
    
    
)


from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [ 
    path('', NuevaReserva.as_view(), name= 'home'),
    path('', include('django.contrib.auth.urls')),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('index/', NuevaReserva.as_view(), name='index'),
    
    


    #URL para las reservas
    path('reservas/create/', ReservaCreateView.as_view(), name='reserva_create'),
    path('reservas/list/', ReservaListView.as_view(), name = 'reserva_list'),
    path('reservas/delete/<int:pk>/', ReservaDeleteView.as_view(), name = 'reserva_delete'),
    path('reservas/update/<int:pk>/', ReservaUpdateView.as_view(), name = 'reserva_update'),
    path('reservas/detail/<int:pk>', ReservaDetailView.as_view(), name= 'reserva_detail'),
    
    
    #URL para los huespedes 
    path('huesped/create/', HuespedCreateView.as_view(), name ='huesped_create'),
    path('huesped/list/', HuespedListView.as_view(), name = 'huesped_list'),
    path('huesped/update/<int:pk>/', HuespedUpdateView.as_view(), name ='huesped_update'),
    path('huesped/delete/<int:pk>/', HuespedDeleteView.as_view(), name ='huesped_delete'),
    path('huesped/detail/<int:pk>/', HuespedDetailView.as_view(), name ='huesped_detail'),
    
    
    #URL para habitaciones
    path('habitacion/create/', HabitacionCreateView.as_view(), name ='habitacion_create'),
    path('habitacion/list/', HabitacionListView.as_view(), name = 'habitacion_list'),
    path('habitacion/update/<int:pk>/', HabitacionUpdateView.as_view(), name ='habitacion_update'),
    path('habitacion/delete/<int:pk>/', HabitacionDeleteView.as_view(), name ='habitacion_delete'),
    path('habitacion/detail/<int:pk>/', HabitacionDetailView.as_view(), name ='habitacion_detail'),
    
    
    ] + static (settings.STATIC_URL, document_root=settings.STATIC_ROOT)