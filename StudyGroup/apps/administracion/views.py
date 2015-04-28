from django.shortcuts import render
from django.views.generic import TemplateView,CreateView,ListView,DetailView,DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Estudiante

# Create your views here.


#class IndexView(TemplateView):
#	template_name='administracion/index.html'

class RegistrarEstudianteView(CreateView):
	template_name = 'estudiante/ingresar.html'
	model = Estudiante
	fields = ['nombre','apellido','direccion']
	success_url = reverse_lazy('est:Listar_Estudiante')
	

class HomeView(TemplateView):
	template_name = "estudiante/index.html"


class ListarEstudianteView(ListView):
	template_name = "estudiante/listarestudiante.html"
	paginate_by = 10
	model = Estudiante

class VerEstudianteView(DetailView):
	model = Estudiante
	template_name = "estudiante/verestudiante.html"
	context_object_name="Estudiante"


class DeleteEstudianteView(DeleteView):
	model = Estudiante
	success_url = reverse_lazy('est:Listar_Estudiante')
	context_object_name = "Estudiante"
	template_name = "estudiante/eliminarestudiante.html"