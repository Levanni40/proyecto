from django.db import models

# Estilo de aplicacion.
class Acerca(models.Model):
    nombre = models.CharField(max_length=50)
    empresa = models.IntegerField()
    
class Servicio(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    email = models.EmailField()
    
class Portfolio(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    email = models.EmailField()
    titulo = models.CharField(max_length=50)
    
class Contactos(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    fechaIngreso = models.DateField()
    recibido = models.BooleanField()            