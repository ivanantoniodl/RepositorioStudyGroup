from django.conf.urls import include, url
from .views import IndexView

urlpatterns = [
	 url(r'^home/',IndexView.as_view()),
   
]
