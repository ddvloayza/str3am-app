from django.urls import path
from django.conf.urls import url
from .views import (home, capitulo_detalle, buscador, app, app_ios)

from .api import CapitulosList, CapitulosDetail

app_name = 'web'

urlpatterns = [
	url(r'^$', home, name='home'),
	url(r'^capitulo/(?P<slug>[-\w]+)/$', capitulo_detalle, name='capitulo_detalle'),
	url(r'^buscador/', buscador, name='buscador'),
	url(r'^app/', app, name='app'),
	url(r'^app-ios/', app_ios, name='app_ios'),

]
