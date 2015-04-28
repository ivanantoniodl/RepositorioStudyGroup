from django.conf.urls import include, url
from .views import  RegistrarEstudianteView,HomeView,ListarEstudianteView,VerEstudianteView, DeleteEstudianteView
urlpatterns = [
	# url(r'^home/',IndexView.as_view()),
	 url(r'^home/$',HomeView.as_view(), name="Home"),
   	 url(r'^add/$',RegistrarEstudianteView.as_view(), name="Registrar_Estudiante"),
   	 url(r'^list/$',ListarEstudianteView.as_view(), name="Listar_Estudiante"),
   	 url(r'^update/(?P<pk>\d+)/$',VerEstudianteView.as_view(), name="Ver_Estudiante"),
   	 url(r'^delete/(?P<pk>\d+)/$',DeleteEstudianteView.as_view(), name="Eliminar_Estudiante"),
]
