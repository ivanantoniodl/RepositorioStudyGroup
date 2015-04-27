from django.db import models

# Create your models here.
class Departamento(models.Model):
	nombre = models.CharField(max_length=45)

	def __unicode__sefl(self):
		return self.nombre