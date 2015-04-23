from django.db import models

class Estudiante(models.Model):
	nombre = models.CharField(max_length=45)
	apellido  = models.CharField(max_length=45)
	direccion = models.CharField(max_length=100)