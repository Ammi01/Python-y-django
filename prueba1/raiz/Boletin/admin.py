from django.contrib import admin

# Register your models here.
from .models import Usuario
from .models import Habitaciones
from .models import Pago
from .models import Reserva

class AdminUsuario(admin.ModelAdmin):
	list_display = ["__str__","nombre","apellido","email","timestamp"]
	class Meta:
		model= Usuario 

admin.site.register(Usuario, AdminUsuario)

class AdminHabitaciones(admin.ModelAdmin):
	list_display = ["num_habitacion","personas","clasificacion","estado"]
	class Meta:
		model= Habitaciones 

admin.site.register(Habitaciones, AdminHabitaciones)


class AdminReserva(admin.ModelAdmin):
	list_display = ["user","personas_por_habitacion","entrada","salida"]
	class Meta:
		model= Reserva 

admin.site.register(Reserva, AdminReserva)



class AdminPago(admin.ModelAdmin):
	list_display = ["referencia","Precio","tipo_pago"]
	class Meta:
		model= Pago 

admin.site.register(Pago, AdminPago)