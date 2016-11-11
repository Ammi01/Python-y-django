from django.db import models

# Create your models here.

class Usuario(models.Model):
	nombre = models.CharField(max_length=100)
	apellido= models.CharField(max_length=100)
	email = models.EmailField()
	dni= models.CharField(max_length=8)
	administrador= models.BooleanField()
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	actualizado=models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self): 
		return "{0} {1}".format (self.dni,self.apellido)


tipoclas=(('1','simple'),('2','matrimonial'),('3','doble'),('4','triple'))
class Habitaciones(models.Model):
	num_habitacion=models.CharField(max_length=3)
	personas= models.IntegerField()
	hab_estado=(('1','ocupada'),('0','desocupada'),)
	estado=models.CharField(max_length=1, choices=hab_estado)
	clasificacion= models.CharField(max_length=1, choices=tipoclas)
		
	def __str__(self): 
		return "{0}".format (self.get_clasificacion_display())

class Reserva(models.Model):
	personas_por_habitacion= models.IntegerField()
	entrada= models.DateField()
	salida= models.DateField()
	user=models.ForeignKey(Usuario)
	habitacion=models.ForeignKey(Habitaciones)
	def __str__(self):
		return "{0}".format (self.personas_por_habitacion)


class Pago(models.Model):
	Precio=models.IntegerField()
	tpago=(('E','efectivo'),('T','tarjeta'),)
	tipo_pago=models.CharField(max_length=1,choices=tpago)
	referencia=models.ForeignKey(Usuario)