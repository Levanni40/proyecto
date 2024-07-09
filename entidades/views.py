from django.shortcuts import render
from .models import*

# Creacion de views.

def home(request):
    return render(request, "entidades/index.html")

def Acerca(request):
    contexto = {"Acerca": Acerca.objects.all()}
    return render(request, "entidades/Acerca.html",contexto)

def Servicio(request):
    return render(request, "entidades/Servicio.html")

def Portfolios(request):
    return render(request, "entidades/Portfolios.html")

def Contactos(request):
    return render(request, "entidades/Contactos.html")