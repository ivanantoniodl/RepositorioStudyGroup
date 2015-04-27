from django.shortcuts import render
from django.views.generic import TemplateView,CreateView,ListView,DetailView,DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Estudiante

# Create your views here.


#class IndexView(TemplateView):
#	template_name='administracion/index.html'

class RegistrarEstudianteView(CreateView):
	template_name = 'administracion/ingresar.html'
	model = Estudiante
	fields = ['nombre','apellido','direccion']
	success_url = reverse_lazy('adm:Listar_Estudiante')
	

class HomeView(TemplateView):
	template_name = "administracion/index.html"


class ListarEstudianteView(ListView):
	template_name = "administracion/listarestudiante.html"
	paginate_by = 2
	model = Estudiante

class VerEstudianteView(DetailView):
	model = Estudiante
	template_name = "administracion/verestudiante.html"
	context_object_name="Estudiante"


class DeleteEstudianteView(DeleteView):
	model = Estudiante
	success_url = reverse_lazy('adm:Listar_Estudiante')
	context_object_name = "Estudiante"
	template_name = "administracion/eliminarestudiante.html"