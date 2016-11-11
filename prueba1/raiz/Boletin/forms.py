from django import forms
from .models import (
	Habitaciones,
	Usuario,
	Reserva,
	Pago,
	)


class FormUsuario(forms.ModelForm):
	class Meta:
		model= Usuario
		fields= ["nombre","apellido","dni","email","administrador"]
		labels={'dni':'DNI',"email":"E-mail"}
		widgets={
		'administrador':forms.CheckboxInput(),
		}


class FormHabitaciones(forms.ModelForm):
	class Meta:
		model= Habitaciones
		fields= ["num_habitacion","clasificacion","estado","personas"]
		labels={
		'num_habitacion': 'Numero de Habitacion',
		'clasificacion':'Clasificación',
		'estado':'Estado',
		'personas':'Numero de personas',
		}

class FormReserva(forms.ModelForm):
	class Meta:
		model= Reserva
		fields= ["user","personas_por_habitacion","entrada",
		"salida","habitacion"]
		labels={
		'user':'Cliente',
		'personas_por-habitacion': 'N° Personas por habitacion',
		'entrada':'Fecha de entrada',
		'salida':'Fecha de salida',
		'habitacion':'Tipo de habitacion',
		}

class FormPago(forms.ModelForm):
	class Meta:
		model= Pago
		exclude = ('exli',)