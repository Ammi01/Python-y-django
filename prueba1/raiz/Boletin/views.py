from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import (
	FormUsuario,
	FormHabitaciones,
	FormReserva,
	FormPago,
	)
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic import ListView, CreateView
from .models import (
	Usuario,
	Habitaciones,
	Reserva,
	Pago,
	)
# Create your views here.
def inicio(request):
	template='inicio.html'
	return render(request,template)

def createUser(request):
	template="create.html"
	queryset=Usuario.objects.all()
	form=FormUsuario(request.POST or None)
	context={
	"queryset":queryset,
	"form":form
	}
	if form.is_valid():
		form.save()
		return HttpResponseRedirect("/listar-clientes/")
	else: form = FormUsuario()

	return render(request, template, context)

def nuevaHabitacion(request):
	template="create.html"
	queryset=Habitaciones.objects.all()
	form=FormHabitaciones(request.POST or None)
	context={
	"queryset":queryset,
	"form":form
	}
	if form.is_valid():
		form.save()
		return HttpResponseRedirect("/habitaciones/")
	else: form = FormUsuario()
	return render(request, template, context)

def nuevaReserva(request):
	template="create.html"
	queryset=Reserva.objects.all()
	form=FormReserva(request.POST or None)
	context={
	"queryset":queryset,
	"form":form,
	}
	if form.is_valid():
		form.save()
		return HttpResponseRedirect("/listar-reservas/")
	else: form = FormReserva()
	return render(request, template, context)

def Pagar(request):
	template="create.html"
	queryset=Pago.objects.all()
	form=FormPago(request.POST or None)
	context={
	"queryset":queryset,
	"form":form
	}
	if form.is_valid():
		form.save()
		return HttpResponseRedirect("/listar-pagos/")
	else: form = FormPago()
	return render(request, template, context)

#creando vistas para Listar

class listaUser(ListView):
	model= Usuario
	template_name= 'usuario_list.html'

class listhabts(ListView):
	model= Habitaciones
	template_name= 'list_habitaciones.html'

class listReserva(ListView):
	model= Reserva
	template_name= 'list_reservas.html'

class listPago(ListView):
	model= Pago
	template_name= 'list_Pago.html'


#Creando vistas para Detalles
class detailUser(DetailView):
	model= Usuario
	template_name = "detail.html"

class detailHabts(DetailView):
	model= Habitaciones
	template_name = "detail_hab.html"

class detailReserva(DetailView):
	model= Reserva
	template_name = "detail_Reser.html"

class detailPago(DetailView):
	model= Pago
	template_name = "detail_Pago.html"

#creando vistass para Update/actualizar
def editarUser(request,pk):
	usuario= Usuario.objects.get(id=pk)
	if request.method =='POST':
		form=FormUsuario(request.POST, instance=usuario)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect('/listar-clientes/')
	else:
		form= FormUsuario(instance=usuario)
	return render(request, 'editar.html', {'form':form})
	

def editarHab(request,pk):
	habitacion= Habitaciones.objects.get(id=pk)
	if request.method =='POST':
		form=FormHabitaciones(request.POST, instance=habitacion)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect('/habitaciones/')
	else:
		form= FormHabitaciones(instance=habitacion)
	return render(request, 'editar.html', {'form':form})

def editarReserva(request,pk):
	reserva= Reserva.objects.get(id=pk)
	if request.method =='POST':
		form=FormReserva(request.POST, instance=reserva)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect('/listar-reservas/')
	else:
		form= FormReserva(instance=reserva)
	return render(request, 'editar.html', {'form':form})

def editarPago(request,pk):
	pago= Pago.objects.get(id=pk)
	if request.method =='POST':
		form=FormPago(request.POST, instance=pago)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect('/listar-pagos/')
	else:
		form= FormPago(instance=pago)
	return render(request, 'editar.html', {'form':form})