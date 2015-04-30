from django.conf.urls import include, url
from django.contrib import admin
from .views import ListarDepartamentoView, AgregarDepartamentoView, EliminarDepartamentoView

urlpatterns = [
    # Examples:
    # url(r'^$', 'StudyGroup.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^departamentos/$', ListarDepartamentoView.as_view(), name='Lista_Departamentos'),
    url(r'^agregar_departamentos/$', AgregarDepartamentoView.as_view(), name='Agregar_Departamento'),
    url(r'^eliminar_departamento/(?P<pk>\d+)/$',EliminarDepartamentoView.as_view(), name='Eliminar_Departamento'),
]
