from django.shortcuts import render
from django.views.generic import TemplateView,CreateView
from .models import Estudiante
# Create your views here.


#class IndexView(TemplateView):
#	template_name='administracion/index.html'

class RegistrarEstudianteView(CreateView):
	template_name = 'administracion/index.html'
	model = Estudiante
	success_url = 
