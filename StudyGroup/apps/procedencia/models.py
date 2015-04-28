from django.db import models

# Create your models here.
class Departamento(models.Model):
	nombre = models.CharField(max_length=45)

	def __unicode__(self):
		return self.nombre

class Municipio(models.Model):
	nombre = models.CharField(max_length=145)
	departamento  = models.ForeignKey(Departamento)

	def __unicode__(self):
		return self.nombre