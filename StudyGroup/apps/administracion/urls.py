from django.conf.urls import include, url
from .views import  RegistrarEstudianteView

urlpatterns = [
	# url(r'^home/',IndexView.as_view()),
	 url(r'^registrar/$',RegistrarEstudianteView.as_view(), name="Registrar_Estudiante"),
   
]
