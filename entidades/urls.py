
from django.urls import path, include
from .views import * 

urlpatterns = [
     path('', home, name="home"),
     path('Acerca', Acerca, name="Acerca"),
     path('Servicio', Servicio, name="Servicio"),
     path('Portfolios', Portfolios, name="Portfolios"),
     path('Contactos', Contactos, name="Contactos"),
]
