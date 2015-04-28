from django.shortcuts import render
from django.views.generic import ListView,CreateView,DeleteView
from .models import Departamento
from django.core.urlresolvers import reverse_lazy

# Create your views here.

class ListarDepartamentoView(ListView):
	template_name= "departamento/listadepartamentos.html"
	model = Departamento;


class AgregarDepartamentoView(CreateView):
	template_name="departamento/agregardepartamento.html"
	model = Departamento;
	fields = ['nombre']
	success_url = reverse_lazy("depto:Lista_Departamentos")

class EliminarDepartamentoView(DeleteView):
	model = Departamento;
	success_url = reverse_lazy("depto:Lista_Departamentos")
	template_name = "departamento/eliminardepartamento.html"
	context_object_name = "Departamento"