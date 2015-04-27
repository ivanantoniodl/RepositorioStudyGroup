from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'StudyGroup.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^',include('apps.administracion.urls',namespace='adm')),
    url(r'^procedencia/',include('apps.procedencia.urls', namespace='procedencia')),

    url(r'^admin/', include(admin.site.urls)),
]
