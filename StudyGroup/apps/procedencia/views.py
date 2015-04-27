from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class ListarDepartamentoView(TemplateView):
	template_name= "procedencia/listadepartamentos.html"