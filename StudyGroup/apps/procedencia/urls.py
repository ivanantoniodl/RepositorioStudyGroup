from django.conf.urls import include, url
from django.contrib import admin
from .views import ListarDepartamentoView, AgregarDepartamentoView, EliminarDepartamentoView

urlpatterns = [
    # Examples:
    # url(r'^$', 'StudyGroup.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^list/$', ListarDepartamentoView.as_view(), name='Lista_Departamentos'),
    url(r'^add/$', AgregarDepartamentoView.as_view(), name='Agregar_Departamento'),
    url(r'^delete/(?P<pk>\d+)/$',EliminarDepartamentoView.as_view(), name='Eliminar_Departamento'),
]
